# Threat model

## Scope and assets

The demo protects access to a private Linux host from GitLab CI and human operators. Assets include the Tailscale auth key, GitLab project and protected variables, runner host, tailnet policy, target's `deploy` account, and deployment/audit records. The demo does not provision the host or alter cloud firewalls.

## Main threats and controls

| Threat | Example control in this project | Operational control still required |
|---|---|---|
| Leaked CI auth key | Masked/protected variable; tagged ephemeral device identity | Limit project scope, rotate/revoke key, review access logs |
| Malicious pipeline change | Protected default branch and manual access job | Require review/approval; restrict who can change CI config |
| Compromised shared runner | Job requires a dedicated runner tag | Use isolated, patched self-managed runner; never share with untrusted workloads |
| Over-broad network reach | CI ACL targets private-host TCP/22 only | Review merged tailnet policy and run negative access tests |
| Privilege escalation on host | CI SSH user is `deploy`, not root | Give deploy minimal local permissions; audit sudo and commands |
| Operator lockout or control-plane outage | Separate human identity path and documented recovery steps | Maintain and test break-glass access before bastion removal |
| Public SSH exposure remains | Runbook calls for staged closure after successful validation | Verify cloud firewall/security group and host firewall changes |

## Residual risks

The auth-key approach relies on a secret even though enrolled CI devices are ephemeral. A compromised runner can use the key while the job is active. Tailnet policy mistakes can grant more access than intended, and a target with an overprivileged `deploy` account can turn SSH access into broader compromise. These risks require environment-specific review, monitoring, and testing; the sample configuration alone does not eliminate them.
