#for apache tomcat

#!/bin/bash
#yum update -y #update the system when launched
#yum install httpd #install apache server
#service httpd start #start the apache server
#chkconfig httpd on  #to automatically start the apache server when the instance starts
#yum install policycoreutils-python #to install policycoreutils-python package in order to add the required SELinux rules for Apache to bind on the new port
read new_port #read custom port number
sudo semanage port -a -t http_port_t -p tcp $new_port  #add the port to SELinux policy configuration
sudo semanage port -m -t http_port_t -p tcp $new_port
sudo service httpd restart #restart the server



#not working gives "SELinux policy is not managed or store cannot be accessed."
