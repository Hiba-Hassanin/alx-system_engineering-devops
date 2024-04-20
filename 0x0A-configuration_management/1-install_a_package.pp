# Puppet manifest to install Flask from pip3

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command     => '/usr/bin/pip3 install Flask==2.1.0',
  path        => ['/usr/bin', '/usr/local/bin'],
  refreshonly => true,
}

# Ensure the package is present after installation
package { 'python3-flask':
  ensure => '2.1.0',
  require => Exec['install_flask'],
}
