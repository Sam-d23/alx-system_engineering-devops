﻿# Puppet automated fix
 
exec { 'Fixing the wordpress site':
  command  => 'sudo sed -i s/.phpp/.php/ /var/www/html/wp-settings.php',
  provider => shell,
}
