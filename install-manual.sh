#!/bin/bash

# Confirmation
    read -n1 -r -p "Press any key to continue..." key;

#
# Pre Install
#

# Install required packages
    sudo yum makecache;
    sudo yum -y install httpd httpd-tools mod_ssl;

#
# Install
#

# Copy main configuration to system
    sudo mkdir -p /etc/apache22deb/conf.d;
    sudo mkdir -p /etc/apache22deb/{mods-available,mods-enabled};
    sudo mkdir -p /etc/apache22deb/{sites-available,sites-enabled};
    sudo cp -r ./SOURCES/apache22deb-1.0.0/etc/apache22deb/* /etc/apache22deb/;

# Copy misc configuration to system
    sudo cp -r ./SOURCES/apache22deb-1.0.0/etc/logrotate.d/* /etc/logrotate.d/;
    sudo cp -r ./SOURCES/apache22deb-1.0.0/etc/bash_completion.d/* /etc/bash_completion.d/;
    sudo cp -r ./SOURCES/apache22deb-1.0.0/etc/sysconfig/* /etc/sysconfig/;
    sudo cp -r ./SOURCES/apache22deb-1.0.0/etc/rc.d/init.d/* /etc/rc.d/init.d/;

# Copy scripts and docs to system
    sudo cp -r ./SOURCES/apache22deb-1.0.0/usr/sbin/* /usr/sbin/;
    sudo chmod +x /usr/sbin/{a2ctl,a2dismod,a2enmod,a2dissite,a2ensite};
    sudo cp -r ./SOURCES/apache22deb-1.0.0/usr/share/man/man8/* /usr/share/man/man8/;
    sudo ln -s /usr/share/man/man8/a2dismod.8.gz /usr/share/man/man8/a2enmod.8.gz
    sudo ln -s /usr/share/man/man8/a2dissite.8.gz /usr/share/man/man8/a2ensite.8.gz

# Create tempoary data directories
    sudo mkdir -p /var/{log,run}/apache22deb;

#
# Post install
#  

# Enable modules
    sudo a2enmod -q log_config alias rewrite dir autoindex;
    sudo a2enmod -q deflate headers expires env setenvif;
    sudo a2enmod -q mime negotiation;
    sudo a2enmod -q suexec ssl;
    sudo a2enmod -q info status;
    sudo a2enmod -q auth_basic authn_file authz_host authz_default authz_user authz_groupfile;
    sudo a2enmod -q actions cgi cgid;

# Enable vhosts
    sudo a2ensite -q default default-ssl;

# Generate default certificate
    sudo /etc/pki/tls/certs/make-dummy-cert /etc/pki/tls/private/apache2.pem; 

# Test configuration
    sudo service apache22deb configtest;

# Output instructions
    echo "Type \`service apache22deb restart\` to restart apache2 httpd";
