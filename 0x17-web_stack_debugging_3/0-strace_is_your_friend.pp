# Puppet automated fix
 
file { '/var/www/html/wp-settings.php':
  ensure  => file,
  content => file('/var/www/html/wp-settings.php').content.gsub('phpp', 'php'),
}
