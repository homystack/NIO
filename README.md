# NixOS Infrastructure Operator (NIO)

A Kubernetes-native operator for declarative management of bare-metal and virtual machines running NixOS.

## Features

- **GitOps Approach**: Configurations are managed through Git repositories
- **Two Application Modes**: Full OS installation and existing system updates
- **State Commitment**: Binding to specific Git commits for reproducibility
- **Safe Deletion**: Clean state removal when configurations are deleted

## CRD (Custom Resource Definitions)

### Machine (`machine.nixos.infra/v1alpha1`)

Manages the state of physical or virtual machines.

### NixosConfiguration (`nixosconfiguration.nixos.infra/v1alpha1`)

Defines NixOS configurations to be applied to machines.

## Installation

```bash
# Apply CRDs
kubectl apply -f crds/

# Build and run the operator
docker build -t nixos-operator:latest .
kubectl apply -f deployment.yaml
```

## Quick Start

1. Create a Machine resource for your target machine
2. Create a NixosConfiguration specifying your Git repository
3. The operator will automatically apply the configuration and commit the hash

## Architecture

The NixOS Infrastructure Operator follows Kubernetes operator patterns to manage NixOS machines declaratively:

- **Machine Resources**: Represent physical or virtual machines with SSH connectivity
- **NixosConfiguration Resources**: Define NixOS configurations from Git repositories
- **GitOps Workflow**: All configurations are version-controlled in Git
- **Commit Tracking**: Every applied configuration is tracked by its Git commit hash

## Key Benefits

- **Reproducibility**: Every system state can be reproduced from Git commits
- **Auditability**: Complete transparency of which configuration versions are running
- **Safety**: Clean state management and safe deletion procedures
- **Automation**: Automated configuration application and monitoring

## Documentation

- [Usage Guide](USAGE.md) - Complete usage instructions and examples
- [Development Guide](DEVELOPMENT.md) - Development and debugging setup
- [Examples](examples/) - Example configurations and machine definitions

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]
