# This Puppet manifest configures Nginx to
# handle high loads efficiently by adjusting default settings.

# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Restart Nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => Package['nginx'],
}

# Modify default Nginx configuration
exec { 'adjust_nginx_default':
  command => '/usr/bin/env sed -i s/15/1000/ /etc/default/nginx',
  notify  => Exec['restart_nginx'],
}

# Restart Nginx to apply changes
exec { 'restart_nginx':
  command     => '/usr/bin/env service nginx restart',
  refreshonly => true,
}
