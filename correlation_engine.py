def run_correlation():
    log_path = "../sample_data/security_events.log"
    failed_count = 0
    target_ip = "192.168.1.100"

    print(f"[*] Ingesting and analyzing logs from: {log_path}\n")

    try:
        with open(log_path, 'r') as file:
            for line in file:
                # Check for failed logons (Event ID 4625)[cite: 6]
                if "EventID: 4625" in line and target_ip in line:
                    failed_count += 1
                    print(f"[!] Alert Rule Triggered: Failed Logon (4625) from {target_ip}. Current count: {failed_count}")

                # Check for successful logon (Event ID 4624) after failures[cite: 6]
                elif "EventID: 4624" in line and target_ip in line:
                    print(f"\n[CORRELATION ALERT] Multi-Event Threshold Reached!")
                    print(f" -> Threat: Brute-Force Attack Followed by Successful Compromise")
                    print(f" -> Source IP: {target_ip}")
                    print(f" -> Total Failed Logons prior to success: {failed_count}")
                    print(f" -> Status: INCIDENT DETECTED\n")
                    break

    except FileNotFoundError:
        print("[-] Error: Log file not found.")

if __name__ == "__main__":
    run_correlation()
