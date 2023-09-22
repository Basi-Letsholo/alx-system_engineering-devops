# executes a command to kill a process

exec { 'killmenow':
  command => 'pkill killmenow',
  user    => 'root',
  path    => '/usr/bin:/bin',
}
