# Puppet manifest to kill a process named killmenow

exec { 'kill_killmenow':
  command     => 'pkill -f killmenow',
  path        => ['/bin', '/usr/bin'],
  onlyif      => 'pgrep -f killmenow',
}
