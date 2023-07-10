# Cybersecurity Analyst at Telstra 
This repository showcases the Day in the Life (DITL) of a cybersecurity analyst at Telstra, a leading telecommunications company based in Australia. The DITL experience focuses on handling a malware attack and includes the following 4 tasks:

### Task 1: Responding to a Malware Attack

- Triaging alerts and promptly responding to a malware attack by coordinating with the appropriate teams.
- Developing skills in incident triage, detection, response, research, communication, data analysis, and teamwork.

### Task 2: Analyzing the Attack

- Conducting a thorough analysis of malware attack data to identify the spread mechanisms and patterns used by the attacker.
- Utilizing network analysis, cybersecurity techniques, data analysis, research, communication, and teamwork.
### Task 3: (Technical) Mitigating the Malware Attack

- Using Python programming skills, designing and implementing firewall rules to prevent the further spread of the malware based on identified patterns.
- Applying software development, Python coding, security engineering, solution architecture, design thinking, and problem-solving abilities.

## Task 4: Incident Postmortem

- Engaging in an incident reflection process to analyze and reflect on the incident's details and outcomes.
- Developing skills in incident reflection, root cause analysis, communication, strategy, governance, risk management, and compliance.

This repository provides solutions, code samples, and example emails for each task to showcase the skills and knowledge gained during the Telstra Cybersecurity Virtual Experience.

# Expansion of the Tasks

## Task 1 (T1): Incident Initation - Awareness and Mitigation

The Incident Initiation Email is the initial communication sent to the respective team responsible for addressing the ongoing malware attack. It provides awareness about the attack and offers mitigation advice to begin the incident response process. The purpose of this task is to triage current malware threats, identify affected infrastructure, and initiate an incident response.

## Task 2 (T2): Firewall Rule Creation Request

The Firewall Rule Creation Request is a communication sent to the respective team responsible for managing the firewall. It outlines the details of the ongoing attack, provides information about the type of traffic to be blocked, and includes any additional research findings on the attack. The purpose of this task is to analyze firewall logs, identify patterns in the attacker's network requests, and request the creation of a firewall rule to mitigate the attack.

## Task 3 (T3) - Firewall Server

This repository contains the solution for Task 3 of the Telstra Cybersecurity Virtual Experience - Firewall Server. The Firewall Server is designed to handle incoming HTTP requests, analyze them for potential malicious headers, and block requests that match the predefined set of bad headers. See "main.py" for the Python code.

## Usage

1. Clone the repository to your local machine:

```shell
git clone https://github.com/track001/TelstraCybersecurityAnalyst.git
```

### Navigate to the cloned repository:
```shell
cd <repository-name>
```
Run the Firewall Server:
```shell
python main.py
```
The Firewall Server will start running on localhost at port 8000.

## Explanation
The Firewall Server code is implemented using Python's built-in http.server module. It extends the BaseHTTPRequestHandler class to handle incoming requests and perform header analysis.

The `block_request` function handles blocking a request and sending a 403 Forbidden response.

The `handle_request` function processes each incoming request. It checks the request path and examines the request headers for potential malicious headers. If a request is on the Spring Framework path and contains any of the predefined bad headers, the request is blocked and a 403 Forbidden response is sent.

The ServerHandler class defines the behavior for different HTTP methods (GET and POST). It calls the handle_request function to process incoming requests.
