###############################################################################
# Package information
###############################################################################
Summary:        apache22deb
Name:           apache22deb
Version:        1.0.0
Release:        0
License:        GPL 2.0
Packager:       Luís Pedro Algarvio <mailto:lp.algarvio@gmail.com>
Group:          Web Server
Source:         -
URL:            -
Requires:       httpd >= 2.2, httpd < 2.3, mod_ssl
BuildArch:      noarch
BuildRoot:      %{_builddir}/%{name}-%{version}

###############################################################################
# Package description
###############################################################################
%description
Installs a Debian-alike apache httpd configuration into a new /etc/apache22deb directory for CentOS/RHEL.
Also provides the Debian scripts for managing modules and vhosts. Targets httpd 2.2 only.


###############################################################################
# Stage: prep
# Read ~/rpmbuild/SOURCES and copy to ~/rpmbuild/BUILD
###############################################################################
%prep

# Initialize setup
%setup -q


###############################################################################
# Stage: build
# Build archives in ~/rpmbuild/BUILD
###############################################################################
%build


###############################################################################
# Stage: check
# Test archives in ~/rpmbuild/BUILD
###############################################################################
%check


###############################################################################
# Stage: install
# Read ~/rpmbuild/BUILD and copy to ~/rpmbuild/BUILDROOT
###############################################################################
%install


###############################################################################
# Macro: clean
# Cleanup after build and install
###############################################################################
%clean

# Cleanup buildroot directory
rm -rf $RPM_BUILD_ROOT


###############################################################################
# Macro: pre-install                                                          #
###############################################################################
%pre

# Stop httpd service
/sbin/service httpd stop


###############################################################################
# Macro: post-install
###############################################################################
%post

# Create symlink for documentation
/bin/ln -f -s /usr/share/man/man8/a2enmod.8.gz /usr/share/man/man8/a2dismod.8.gz
/bin/ln -f -s /usr/share/man/man8/a2ensite.8.gz /usr/share/man/man8/a2dissite.8.gz

# Enable pluggagle modules
/usr/sbin/a2enmod -q log_config alias rewrite dir autoindex
/usr/sbin/a2enmod -q deflate headers expires env setenvif
/usr/sbin/a2enmod -q mime negotiation
/usr/sbin/a2enmod -q suexec ssl
/usr/sbin/a2enmod -q info status
/usr/sbin/a2enmod -q auth_basic authn_file authz_host authz_default authz_user authz_groupfile
/usr/sbin/a2enmod -q actions cgi cgid

# Enable pluggagle vhosts
/usr/sbin/a2ensite -q default default-ssl

# Generate default certificate
/etc/pki/tls/certs/make-dummy-cert /etc/pki/tls/private/apache2.pem

# Test configuration and restart apache22deb service
/sbin/service apache22deb configtest
/sbin/service apache22deb restart


###############################################################################
# Macro: pre-uninstall
###############################################################################
%preun

# Stop apache22deb service
/sbin/service apache22deb stop


###############################################################################
# Macro: post-uninstall
###############################################################################
%postun

# Test configuration and restart httpd service
/sbin/service httpd configtest
/sbin/service httpd restart


###############################################################################
# Data: Binaries and scripts (/usr/sbin)
###############################################################################
%files

# Bundled scripts (a2ctl, a2en*, a2dis*)
%defattr(755, root, root)
/usr/sbin/a2ctl
/usr/sbin/a2dismod
/usr/sbin/a2dissite
/usr/sbin/a2enmod
/usr/sbin/a2ensite


###############################################################################
# Data: Documentation (/usr/share)
###############################################################################

# Docs for scripts (a2ctl, a2en*, a2dis*)
%doc
%defattr(644, root, root)
/usr/share/man/man8/a2ctl.8.gz
/usr/share/man/man8/a2enmod.8.gz
/usr/share/man/man8/a2ensite.8.gz


###############################################################################
# Data: Configuration (/etc)
###############################################################################

# Main configuration (/etc/apache22deb)
%config
%defattr(644, root, root)
/etc/apache22deb/apache2.conf
/etc/apache22deb/envvars
/etc/apache22deb/magic
/etc/apache22deb/ports.conf

# Other configuration (/etc/apache22deb/conf.d)
%config
%defattr(644, root, root)
/etc/apache22deb/conf.d/charset
/etc/apache22deb/conf.d/localized-error-pages
/etc/apache22deb/conf.d/other-vhosts-access-log
/etc/apache22deb/conf.d/security

# Pluggable modules (/etc/apache22deb/mods-available)
%config
%defattr(644, root, root)
/etc/apache22deb/mods-available/actions.conf
/etc/apache22deb/mods-available/actions.load
/etc/apache22deb/mods-available/alias.conf
/etc/apache22deb/mods-available/alias.load
/etc/apache22deb/mods-available/asis.load
/etc/apache22deb/mods-available/auth_basic.load
/etc/apache22deb/mods-available/auth_digest.load
/etc/apache22deb/mods-available/authn_alias.load
/etc/apache22deb/mods-available/authn_anon.load
/etc/apache22deb/mods-available/authn_dbd.load
/etc/apache22deb/mods-available/authn_dbm.load
/etc/apache22deb/mods-available/authn_default.load
/etc/apache22deb/mods-available/authn_file.load
/etc/apache22deb/mods-available/authnz_ldap.load
/etc/apache22deb/mods-available/authz_dbm.load
/etc/apache22deb/mods-available/authz_default.load
/etc/apache22deb/mods-available/authz_groupfile.load
/etc/apache22deb/mods-available/authz_host.load
/etc/apache22deb/mods-available/authz_owner.load
/etc/apache22deb/mods-available/authz_user.load
/etc/apache22deb/mods-available/autoindex.conf
/etc/apache22deb/mods-available/autoindex.load
/etc/apache22deb/mods-available/cache.load
/etc/apache22deb/mods-available/cern_meta.load
/etc/apache22deb/mods-available/cgi.load
/etc/apache22deb/mods-available/cgid.conf
/etc/apache22deb/mods-available/cgid.load
/etc/apache22deb/mods-available/charset_lite.load
/etc/apache22deb/mods-available/dav.load
/etc/apache22deb/mods-available/dav_fs.conf
/etc/apache22deb/mods-available/dav_fs.load
/etc/apache22deb/mods-available/dav_lock.load
/etc/apache22deb/mods-available/dbd.load
/etc/apache22deb/mods-available/deflate.conf
/etc/apache22deb/mods-available/deflate.load
/etc/apache22deb/mods-available/dir.conf
/etc/apache22deb/mods-available/dir.load
/etc/apache22deb/mods-available/disk_cache.conf
/etc/apache22deb/mods-available/disk_cache.load
/etc/apache22deb/mods-available/dump_io.load
/etc/apache22deb/mods-available/env.load
/etc/apache22deb/mods-available/expires.load
/etc/apache22deb/mods-available/ext_filter.load
/etc/apache22deb/mods-available/fcgid.conf
/etc/apache22deb/mods-available/fcgid.load
/etc/apache22deb/mods-available/file_cache.load
/etc/apache22deb/mods-available/filter.load
/etc/apache22deb/mods-available/headers.load
/etc/apache22deb/mods-available/ident.load
/etc/apache22deb/mods-available/imagemap.load
/etc/apache22deb/mods-available/include.load
/etc/apache22deb/mods-available/info.conf
/etc/apache22deb/mods-available/info.load
/etc/apache22deb/mods-available/ldap.conf
/etc/apache22deb/mods-available/ldap.load
/etc/apache22deb/mods-available/log_config.load
/etc/apache22deb/mods-available/log_forensic.load
/etc/apache22deb/mods-available/logio.load
/etc/apache22deb/mods-available/mem_cache.conf
/etc/apache22deb/mods-available/mem_cache.load
/etc/apache22deb/mods-available/mime.conf
/etc/apache22deb/mods-available/mime.load
/etc/apache22deb/mods-available/mime_magic.conf
/etc/apache22deb/mods-available/mime_magic.load
/etc/apache22deb/mods-available/negotiation.conf
/etc/apache22deb/mods-available/negotiation.load
/etc/apache22deb/mods-available/proxy.conf
/etc/apache22deb/mods-available/proxy.load
/etc/apache22deb/mods-available/proxy_ajp.load
/etc/apache22deb/mods-available/proxy_balancer.conf
/etc/apache22deb/mods-available/proxy_balancer.load
/etc/apache22deb/mods-available/proxy_connect.load
/etc/apache22deb/mods-available/proxy_ftp.conf
/etc/apache22deb/mods-available/proxy_ftp.load
/etc/apache22deb/mods-available/proxy_http.load
/etc/apache22deb/mods-available/proxy_scgi.load
/etc/apache22deb/mods-available/reqtimeout.conf
/etc/apache22deb/mods-available/reqtimeout.load
/etc/apache22deb/mods-available/rewrite.load
/etc/apache22deb/mods-available/setenvif.conf
/etc/apache22deb/mods-available/setenvif.load
/etc/apache22deb/mods-available/speling.load
/etc/apache22deb/mods-available/ssl.conf
/etc/apache22deb/mods-available/ssl.load
/etc/apache22deb/mods-available/status.conf
/etc/apache22deb/mods-available/status.load
/etc/apache22deb/mods-available/substitute.load
/etc/apache22deb/mods-available/suexec.load
/etc/apache22deb/mods-available/unique_id.load
/etc/apache22deb/mods-available/userdir.conf
/etc/apache22deb/mods-available/userdir.load
/etc/apache22deb/mods-available/usertrack.load
/etc/apache22deb/mods-available/version.load
/etc/apache22deb/mods-available/vhost_alias.load

# Pluggable vhosts (/etc/apache22deb/sites-available)
%config
%defattr(644, root, root)
/etc/apache22deb/sites-available/default
/etc/apache22deb/sites-available/default-ssl

# System integration (/etc/*)
%config
%defattr(644, root, root)
/etc/bash_completion.d/apache22deb
/etc/logrotate.d/apache22deb
/etc/sysconfig/apache22deb
%defattr(755, root, root)
/etc/rc.d/init.d/apache22deb


###############################################################################
# Data: Directories (...)
###############################################################################

# Configuration (/etc/apache22deb)
%dir
%defattr(755, root, root)
/etc/apache22deb
/etc/apache22deb/conf.d
/etc/apache22deb/mods-available
/etc/apache22deb/mods-enabled
/etc/apache22deb/sites-available
/etc/apache22deb/sites-enabled

# Logs (/var/log/apache22deb)
%dir
%defattr(700, root, root)
/var/log/apache22deb

# Temporary data (/var/run/apache22deb)
%dir
%defattr(700, root, apache)
/var/run/apache22deb


###############################################################################
# The changes log
###############################################################################
%changelog

