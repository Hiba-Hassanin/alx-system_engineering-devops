# Web Stack Debugging

This project involves debugging and optimizing a web stack using Puppet manifests. The goal is to ensure that our Nginx server can handle a high number of requests without failure.

## Requirements
- Ubuntu 14.04 LTS
- Puppet v3.4
- `puppet-lint` v2.1.1

## Instructions
1. Ensure Puppet is installed.
2. Run the provided Puppet manifest to configure Nginx.
3. Use ApacheBench to test the server's performance.
4. Verify that there are no failed requests.

## Usage
To apply the Puppet manifest, run:
```sh
puppet apply 0-the_sky_is_the_limit_not.pp
