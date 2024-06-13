# Fix Nginx limits by increasing the ULIMIT and restarting the service

# Increase the ULIMIT in the default Nginx configuration file
exec { 'increase_nginx_ulimit':
  command => '/usr/bin/env sed -i "s/15/2000/" /etc/default/nginx',
  path    => ['/usr/bin', '/bin'],
  onlyif  => 'grep -q "15" /etc/default/nginx',  # Only run if "15" is found in the file
} ->

# Restart Nginx to apply the new ULIMIT
exec { 'restart_nginx':
  command => '/usr/bin/env service nginx restart',
  path    => ['/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  refreshonly => true,  # Only restart if the previous exec ran
  subscribe   => Exec['increase_nginx_ulimit'],  # Ensure this runs after the previous exec
}

