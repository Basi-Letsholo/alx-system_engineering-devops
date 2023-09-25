# sets up client ssh config file

file { '~/.ssh/school'
  ensure  => 'present',
  mode    => '0600',
  content => 'Host 54.160.90.222',
  content => '	IdentityFile ~/.ssh/school',
  content => '	PasswordAuthentication no',
}
