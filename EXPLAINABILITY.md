# GitPatentGuard Explainability Specification

This document provides a transparent, verifiable architectural breakdown of how **GitPatentGuard** operates, processes input, makes decisions, and enforces security boundaries.

---

## 1. Input Data and Data Sources Used

GitPatentGuard consumes USPTO and EPO published patent applications, patent examiner rejection actions, technical invention disclosure forms, and maintenance fee fee schedules. These data sources include claim text narratives, filing date timestamps, International Patent Classification (IPC) codes, and inventor assignment records. The agent ingests these inputs in raw text, XML, and JSON metadata format and parses them into standardized patent claim models for downstream legal analysis. Patent litigation databases and prior art registries are also monitored as sensitive data sources to ensure freedom-to-operate standards are strictly maintained.

---

## 2. How It Decides and Reasoning Process

The decision making process follows a deterministic, five-stage analytical pipeline designed to eliminate ambiguity and hallucination. When an invention disclosure or draft claim set is analyzed, the agent first evaluates prior art overlap using the prior-art-similarity-scorer tool to identify anticipation or obviousness risks. Next, the reasoning engine invokes the claim-breadth-analyzer tool to measure limitation count and structural claim breadth. Furthermore, statutory patent lifespans and maintenance deadlines are calculated using the patent-expiration-calculator tool. Finally, the agent correlates all IP metrics against predefined patentability standards to issue a conclusive verdict of APPROVED, BLOCKED, or NEEDS_REVIEW alongside an automated prosecution strategy report.

---

## 3. Constraints, Limitations, and Known Issues

GitPatentGuard operates under strict operational constraints to prevent false positives and non-deterministic behavior across different agent frameworks. GitPatentGuard operates under strict operational constraints to prevent costly intellectual property litigation and invalid patent filings. The agent is deliberately limited to patent text parsing and statutory rule calculation and cannot appear before patent examiners or litigate in courtrooms. Another known issue and limitation is that newly filed secret provisional applications within the 18-month publication blackout window cannot be indexed. Furthermore, the agent enforces a low temperature constraint of 0.1 to maintain strict predictability across all supported export frameworks.
