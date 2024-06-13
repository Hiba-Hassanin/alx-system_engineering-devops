# This Puppet manifest increases
# the open files limit for the holberton user.

# Ensure the limits.conf file is updated to
# increase the open files limit for holberton user
exec { 'increase_open_files_limit':
  command => '/usr/bin/env sed -i "/holberton/ s/^.*$/holberton soft nofile 4096\\nholberton hard nofile 8192/" /etc/security/limits.conf',
  onlyif  => '/usr/bin/env grep -q "holberton" /etc/security/limits.conf',
}

# Ensure the common-session file is updated to include pam_limits.so
file_line { 'add pam_limits to common-session':
  path  => '/etc/pam.d/common-session',
  line  => 'session required pam_limits.so',
  match => '^session\s+required\s+pam_limits.so',
}
