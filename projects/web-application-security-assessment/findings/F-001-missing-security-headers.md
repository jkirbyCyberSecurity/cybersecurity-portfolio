# F-001: Missing Browser Security Headers

## Status
Observed — remediation recommended; exploitability not demonstrated.

## Severity
Informational / Low (provisional)

## Affected Component
Kirby Security Lab HTTP response at http://127.0.0.1:8000/

## Observation
The baseline HTTP response did not include the following headers:
- Content-Security-Policy
- X-Content-Type-Options
- X-Frame-Options

Evidence is stored in:
- evidence/baseline-security-headers.txt
- evidence/baseline-http-response.txt

## Potential Impact
Without appropriate browser security headers, an application may have fewer
defense-in-depth protections against certain classes of browser-based attacks.
The impact depends on the application's functionality and other existing controls.

## Recommendation
Evaluate and configure suitable headers:
- Content-Security-Policy: restrict permitted content sources.
- X-Content-Type-Options: nosniff.
- X-Frame-Options: DENY, or use an appropriate CSP frame-ancestors directive.

Choose policies that match the application's actual requirements and test them
for compatibility before deployment.

## Validation
Initial baseline only. No exploit was demonstrated.
Retest after remediation and record the results.

## Scope
Authorized local lab only; target bound to 127.0.0.1.
