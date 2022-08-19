exec { 'killmenow':
    provider => 'shell',
    command  => 'pkill -f 'killmenow''
}
