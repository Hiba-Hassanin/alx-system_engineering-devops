# This Puppet manifest increases the open files limit for the holberton user.

# Ensure the limits.conf file is updated with the new limits
file { '/etc/security/limits.conf':
  ensure  => present,
  content => template('user_limit/limits.conf.erb'),
}

# Ensure the common-session file is updated to include pam_limits.so
file_line { 'add pam_limits to common-session':
  path  => '/etc/pam.d/common-session',
  line  => 'session required pam_limits.so',
  match => '^session\s+required\s+pam_limits.so',
}
