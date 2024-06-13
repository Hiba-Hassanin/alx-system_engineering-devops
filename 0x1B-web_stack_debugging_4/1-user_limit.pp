# Increases the amount of traffic an Nginx server
# can handle by increasing the ULIMIT.

# Increase the ULIMIT in the default Nginx configuration file
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/usr/local/bin', '/bin'],
  onlyif  => 'grep -q "15" /etc/default/nginx',  # Only run if "15" is found in the file
} ->

# Restart Nginx to apply the new ULIMIT
exec { 'nginx-restart':
  command => 'service nginx restart',
  path    => ['/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  refreshonly => true,  # Only restart if the previous exec ran
  subscribe   => Exec['fix--for-nginx'],  # Ensure this runs after the previous exec
}
