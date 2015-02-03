#!/bin/bash

# Confirmation
    read -n1 -r -p "Press any key to continue..." key;

#
# Pre Install
#

# Install required packages
    yum makecache;
    yum -y install httpd httpd-tools mod_ssl;

#
# Install
#

# Copy main configuration to system
    mkdir -p /etc/apache2deb/conf.d;
    mkdir -p /etc/apache2deb/{mods-available,mods-enabled};
    mkdir -p /etc/apache2deb/{sites-available,sites-enabled};
    cp -r ./data/etc/apache2deb/* /etc/apache2deb/;

# Copy misc configuration to system
    cp -r ./data/etc/logrotate.d/* /etc/logrotate.d/;
    cp -r ./data/etc/bash_completion.d/* /etc/bash_completion.d/;
    cp -r ./data/etc/sysconfig/* /etc/sysconfig/;
    cp -r ./data/etc/rc.d/init.d/* /etc/rc.d/init.d/;

# Copy scripts and docs to system
    cp -r ./data/usr/sbin/* /usr/sbin/;
    chmod +x /usr/sbin/{a2ctl,a2dismod,a2enmod,a2dissite,a2ensite};
    cp -r ./data/usr/share/man/man8/* /usr/share/man/man8/;
    ln -s /usr/share/man/man8/a2dismod.8.gz /usr/share/man/man8/a2enmod.8.gz
    ln -s /usr/share/man/man8/a2dissite.8.gz /usr/share/man/man8/a2ensite.8.gz

# Create tempoary data directories
    mkdir -p /var/{log,run}/apache2deb;

#
# Post install
#  

# Enable modules
    a2enmod -q log_config alias rewrite dir autoindex;
    a2enmod -q deflate headers expires env setenvif;
    a2enmod -q mime negotiation;
    a2enmod -q suexec ssl;
    a2enmod -q info status;
    a2enmod -q auth_basic authn_file authz_host authz_default authz_user authz_groupfile;
    a2enmod -q actions cgi cgid;

# Enable vhosts
    a2ensite -q default default-ssl;

# Generate default certificate
    /etc/pki/tls/certs/make-dummy-cert /etc/pki/tls/private/apache2.pem; 

# Test configuration
    service apache2deb configtest;

# Output instructions
    echo "Type `service apache2deb restart` to restart apache2 httpd";
