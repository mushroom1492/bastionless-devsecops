# Bastion retirement runbook

This is a controlled migration outline, not an automated production change. Treat public SSH/firewall changes as a change-managed operation.

## Before changing access

- Inventory bastion-dependent users, jobs, network routes, audit requirements, and emergency access paths.
- Confirm all target machines are supported Linux hosts and can maintain Tailscale connectivity.
- Define owners for tailnet tags, the GitLab runner, target account, auth-key rotation, and incident response.
- Decide how to monitor connectivity and SSH events, and how to revoke a compromised device or credential.

## Pilot

1. Configure the example tags and least-privilege policy in a non-production tailnet or test environment.
2. Enroll one non-production Linux target as `tag:private-host` and verify Tailscale SSH with an operator identity.
3. Configure a dedicated trusted runner with TUN access. Protect the default branch and CI variables.
4. Run policy tests and the protected manual smoke job. Confirm the target command runs under `deploy` and does not have unintended sudo privileges.
5. Test denied paths: CI to non-SSH ports, unauthorized users to the target, and root login.
6. Test revocation: remove the CI key/device or change policy and verify access stops. Test recovery with an independent break-glass path.

## Gradual rollout

- Migrate a small, low-risk host group first. Preserve existing access temporarily.
- Observe connection reliability, access logs, support tickets, and recovery readiness across a representative period.
- Expand by service/team only after success criteria are met and approvals are recorded.
- Remove bastion inbound SSH and associated public exposure only after owners confirm replacement access and rollback.
- Decommission the bastion after confirming no remaining workflows depend on it; remove its keys, routes, DNS records, and infrastructure through the normal change process.

## Rollback

If operators or automation lose needed access, use the pre-approved break-glass route; do not weaken the tailnet policy globally. Restore the previously approved access path through change management, troubleshoot runner/device approval, policy, host firewall, and target account separately, and re-test before resuming rollout.

## Completion criteria

- No public inbound SSH is required for the migrated workload.
- Human and CI access are independently attributable and least-privilege.
- Unauthorized network/SSH paths are tested and denied.
- Logs and alert ownership are documented.
- Revocation, emergency recovery, and rollback have been exercised.
- Bastion dependencies are removed, not merely left as undocumented fallback paths.
