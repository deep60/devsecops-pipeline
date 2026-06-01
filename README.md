# DevSecOps CI/CD Security Pipeline

Automated security scanning pipeline built with GitHub Actions.
Every push triggers 5 security tools before deployment is allowed.

## Pipeline Architecture

SAST → Secrets → Container Scan + IaC Scan + Dependency Scan → Security Gate

## Tools & Results

| Tool       | Scope               | Findings on test app         |
|------------|---------------------|------------------------------|
| Semgrep    | Source code (SAST)  | SQL injection, command injection |
| TruffleHog | Git history         | Credential leak detection    |
| Trivy      | Docker image        | 230 CVEs (8 CRITICAL)        |
| Checkov    | Terraform IaC       | 22 misconfigurations         |
| Trivy SCA  | Python dependencies | Outdated packages with CVEs  |

## Security Gate

Deployment is automatically blocked if:
- Container has >10 unresolved CRITICAL CVEs
- IaC has >20 failed security checks

## Stack

GitHub Actions · Semgrep · TruffleHog · Trivy · Checkov · Docker
