# Verification & Break Test Evidence

## Baseline Check
- Verified repository structure contains backend/, frontend/, tests/, and docs/.

## Backend Test Results
- Ran pytest successfully, validating root endpoint, task creation with tags/due dates, and overdue filtering.

## Manual Browser Checks
- Opened frontend/index.html to confirm tasks load correctly with tag badges and due dates.

## Break Test Evidence
- Tested invalid date formats and non-existent task IDs; verified proper HTTP error codes (400/404) are returned.
