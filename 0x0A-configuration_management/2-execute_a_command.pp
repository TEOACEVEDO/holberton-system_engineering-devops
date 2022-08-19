# Using Puppet, create a manifest that kills a process named killmenow

exec { 'killmenow':
    provider => 'shell',
    command  => 'pkill -f 'killmenow''
}
