# Installs flask from pip3 using puppet

exec { 'install_package':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => '/usr/local/bin:/usr/bin:/bin',
  user    => 'root',
}
