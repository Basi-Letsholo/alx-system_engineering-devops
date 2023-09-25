# sets up client ssh config file

file { 'ubuntu/~/etc/ssh/ssh_config':
  ensure  => 'present',
  mode    => '0600',
  owner   => 'ubuntu',
  content => "
    Host 54.160.90.222
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
