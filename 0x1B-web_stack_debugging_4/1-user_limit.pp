# Fix Nginx limits by increasing the ULIMIT and restarting the service

exec { '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf': }
