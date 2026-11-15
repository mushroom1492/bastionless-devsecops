# LinkedIn project showcase

## Post draft

**Building a bastionless DevSecOps access pattern with GitLab CI and Tailscale**

I’ve been exploring how to reduce reliance on traditional bastion hosts without losing control over who can reach private infrastructure.

This GitLab project demonstrates a simple pattern:

- GitLab CI joins a private Tailscale network as a tagged, ephemeral node.
- Tailnet policy limits CI to SSH on private hosts, and Tailscale SSH limits it to a dedicated `deploy` account.
- Human operators use a separate identity-based rule with re-authentication.
- CI runs a protected, manual, read-only access check—no public inbound SSH path is needed for the demo.

The repository includes the pipeline, sample access policy, validation tests, architecture diagram, and a staged migration runbook. It deliberately uses a protected Tailscale auth key according to the documented GitLab integration, rather than claiming an unsupported OIDC setup.

This is a demonstration, not a production rollout. A real migration still needs a trusted runner, protected/rotated credentials, break-glass access, monitoring, and a tested rollback before retiring a bastion.

I’d be interested in how others are approaching bastion reduction and private CI/CD access.

#DevSecOps #GitLab #Tailscale #ZeroTrust #CloudSecurity #PlatformEngineering

## Suggested project description

A bastionless access pattern for GitLab CI and private Linux infrastructure using Tailscale, Tailscale SSH, least-privilege policy, and ephemeral CI nodes.

## Suggested pinned comment

Project source: add the GitLab repository URL here after importing the starter. The README includes setup requirements and explains the demo boundaries.

## Before posting

- Import the repository to GitLab and make it public only if your policies allow it.
- Replace this starter's example email and confirm the tailnet policy against your own environment.
- Do not post auth keys, target hostnames, IP addresses, runner credentials, or screenshots containing secrets.
- If you have not run it against a real GitLab/Tailscale environment, describe it as a design/demo project rather than a deployed production solution.
