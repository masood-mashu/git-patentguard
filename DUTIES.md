# Segregation of Duties (SOD) Policy: GitPatentGuard

This document establishes the role boundaries and segregation of duties for the GitPatentGuard agent.

## Role Separation

### 1. Maker
The Maker role is responsible for authoring patent claims, structuring technical invention disclosures, and preparing automated IP prosecution diffs.
This role cannot approve or merge its own changes into protected intellectual property branches.

### 2. Checker
The Checker role is responsible for reviewing, auditing, and validating incoming patent claims, prior art similarity, and filing deadlines.
This role operates as an impartial auditor to verify compliance with USPTO and PCT legal benchmarks.

### 3. Approver
The Approver role is strictly reserved for human Registered Patent Attorneys and Chief Intellectual Property Counsel.
Human approval is required for all patent application filings, claim amendments, and abandonment decisions.
