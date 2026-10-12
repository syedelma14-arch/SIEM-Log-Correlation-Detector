# SIEM Multi-Event Correlation Detector

A beginner-friendly security project simulating a SIEM multi-event correlation engine to detect brute-force attacks followed by successful account compromises.

## Project Overview
In modern Security Operations Center (SOC) environments, analyzing massive volumes of security logs manually is inefficient. This project mimics automated SIEM threat detection rules by parsing Windows security event logs to track malicious authentication patterns.

## Features
- **Log Parsing:** Ingests normalized log streams to extract critical attributes like `EventID`, `TargetUserName`, and `IpAddress`.
- **Multi-Event Correlation:** Aggregates multiple failed login attempts (`Event ID 4625`) followed by a successful logon (`Event ID 4624`) from the same source IP to flag a potential breach.

## Files
- `scripts/correlation_engine.py`: The core Python script executing the detection logic.
- `sample_data/security_events.log`: Normalized sample security events used for testing.
