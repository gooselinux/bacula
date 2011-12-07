%define working_dir	/var/spool/bacula
%define script_dir	/usr/libexec/bacula
#%define rescue_version	2.0.0
%define docs_version	%{version}
%define gui_version	%{version}
%define config_dir	%{_sysconfdir}/bacula

Summary: Cross platform network backup for Linux, Unix, Mac and Windows
Name: bacula
Version: 5.0.0
Release: 7%{?dist}
# See LICENSE for details
License: GPLv2 with exceptions
Group: System Environment/Daemons
Source0: http://downloads.sourceforge.net/project/bacula/bacula/%{version}/bacula-%{version}.tar.gz
Source1: http://downloads.sourceforge.net/project/bacula/bacula/%{docs_version}/bacula-docs-%{docs_version}.tar.bz2
#this link will be active after the release gets old
#Source0: http://downloads.sourceforge.net/project/bacula/z-older-releases/bacula/%{version}/bacula-%{version}.tar.gz
#Source1: http://downloads.sourceforge.net/project/bacula/z-older-releases/bacula/%{docs_version}/bacula-docs-%{docs_version}.tar.bz2
#Source2: http://download.sourceforge.net/bacula/bacula-rescue-%{rescue_version}.tar.gz
#Source3: bacula-gconsole.desktop
#Source4: bacula-wxconsole.desktop
Source5: bacula-traymonitor.desktop
Source6: bacula.logrotate
Source7: bacula-fd.init
Source8: bacula-dir.init
Source9: bacula-sd.init
#Source10: http://download.sourceforge.net/bacula/bacula-gui-%{gui_version}.tar.gz
#Source11: bacula-web.apache
Source12: bacula-bat.desktop
Source13: bacula-traymonitor.console_apps
Patch0: bacula-director-configuration.patch
Patch1: bacula-config.patch
#Patch2: bacula-wxconsole.patch
Patch3: bacula-pamd.patch
#Patch4: 2.0.3-ampm.patch
#Patch5: 2.0.3-maxbyteslist.patch
#Patch6: 2.0.3-maxwaittime.patch
#Patch7: 2.0.3-scheduler-next-hour.patch
#Patch8: 2.0.3-verify.patch
#Patch9: 2.0.3-tls-disconnect.patch
#Patch10: bacula-web-smarty.patch
#Patch11: bacula-2.4.3-orphaned-jobs.patch
#Patch12: bacula-2.4.3-python26.patch
Patch13: bacula-3.0.2-openssl.patch
URL: http://www.bacula.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: openssl-devel, atk-devel, ncurses-devel, pango-devel, perl
BuildRequires: libstdc++-devel, libxml2-devel, zlib-devel, pkgconfig
BuildRequires: gtk2-devel, libgnomeui-devel, GConf2-devel
BuildRequires: glibc-devel, ORBit2-devel, libart_lgpl-devel, freetype-devel
BuildRequires: libbonobo-devel, libbonoboui-devel, bonobo-activation-devel
BuildRequires: mysql-devel, cdrecord, postgresql-devel
BuildRequires: desktop-file-utils, python-devel, sqlite-devel, sed,
BuildRequires: libacl-devel, latex2html, tetex-latex, tetex, ghostscript
BuildRequires: dvipdfm, qwt-devel

%if 0%{?fedora} >= 7 || 0%{?rhel} >= 6
BuildRequires: tcp_wrappers-devel
%else
BuildRequires: tcp_wrappers
%endif

%description
Bacula is a set of programs that allow you to manage the backup,
recovery, and verification of computer data across a network of
different computers. It is based on a client/server architecture and is
efficient and relatively easy to use, while offering many advanced
storage management features that make it easy to find and recover lost
or damaged files.


%package director-mysql
Summary: Bacula Director with MySQL database support
Group: System Environment/Daemons
Provides: bacula-director = %{version}-%{release}
Requires: bacula-director-common = %{version}-%{release}
Requires: bacula-common = %{version}-%{release}

%description director-mysql
Bacula is a set of programs that allow you to manage the backup,
recovery, and verification of computer data across a network of
different computers. It is based on a client/server architecture.

This package contains the bacula director, the server which controls 
your backup run.
This director has support for the MySQL database.


%package director-sqlite
Summary: Bacula Director with sqlite database support
Group: System Environment/Daemons
Provides: bacula-director = %{version}-%{release}
Requires: bacula-director-common = %{version}-%{release}
Requires: bacula-common = %{version}-%{release}

%description director-sqlite
Bacula is a set of programs that allow you to manage the backup,
recovery, and verification of computer data across a network of
different computers. It is based on a client/server architecture.

This package contains the bacula director, the server which controls 
your backup run.
This director has support for the sqlite database.


%package director-postgresql
Summary: Bacula Director with PostgresSQL database support
Group: System Environment/Daemons
Provides: bacula-director = %{version}-%{release}
Requires: bacula-director-common = %{version}-%{release}
Requires: bacula-common = %{version}-%{release}

%description director-postgresql
Bacula is a set of programs that allow you to manage the backup,
recovery, and verification of computer data across a network of
different computers. It is based on a client/server architecture.

This package contains the bacula director, the server which controls 
your backup run.
This director has support for the PostgresSQL database.


%package director-common
Summary: Common Bacula Director files
Group: System Environment/Daemons
Requires: bacula-director = %{version}-%{release}
Requires: bacula-common = %{version}-%{release}
Requires: logwatch
#Requires(pre): fedora-usermgmt
#Requires(postun): fedora-usermgmt

%description director-common
Bacula is a set of programs that allow you to manage the backup,
recovery, and verification of computer data across a network of
different computers. It is based on a client/server architecture.

This package contains the common director files, which are shared 
between all database backends. You have to select a possible
database backend though, which provides the needed bacula-director
dependency. Please choose from bacula-director-mysql,
bacula-director-sqlite or bacula-director-postgresql.


%package client
Summary: Bacula backup client
Group: System Environment/Daemons
Requires: bacula-common = %{version}-%{release}
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service
Requires(postun): /sbin/service

%description client
Bacula is a set of programs that allow you to manage the backup,
recovery, and verification of computer data across a network of
different computers. It is based on a client/server architecture.

This package contains the bacula client, the daemon running on the 
system to be backed up.


%package storage-common
Summary: Common Bacula storage daemon files
Group: System Environment/Daemons
Requires: bacula-storage = %{version}-%{release}
Requires: bacula-common = %{version}-%{release}

%description storage-common
Bacula is a set of programs that allow you to manage the backup,
recovery, and verification of computer data across a network of
different computers. It is based on a client/server architecture.

This package contains the storage daemon, the daemon responsible for 
writing the data received from the clients onto tape drives or other 
mass storage devices.


%package storage-mysql
Summary: MySQL Bacula storage daemon files
Group: System Environment/Daemons
Provides: bacula-storage = %{version}-%{release}
Requires: bacula-storage-common = %{version}-%{release}
Requires: bacula-common = %{version}-%{release}

%description storage-mysql
Bacula is a set of programs that allow you to manage the backup,
recovery, and verification of computer data across a network of
different computers. It is based on a client/server architecture.

This package contains the storage daemon, the daemon responsible for 
writing the data received from the clients onto tape drives or other 
mass storage devices.


%package storage-sqlite
Summary: SQLite Bacula storage daemon files
Group: System Environment/Daemons
Provides: bacula-storage = %{version}-%{release}
Requires: bacula-storage-common = %{version}-%{release}
Requires: bacula-common = %{version}-%{release}

%description storage-sqlite
Bacula is a set of programs that allow you to manage the backup,
recovery, and verification of computer data across a network of
different computers. It is based on a client/server architecture.

This package contains the storage daemon, the daemon responsible for 
writing the data received from the clients onto tape drives or other 
mass storage devices.


%package storage-postgresql
Summary: Common Bacula storage daemon files
Group: System Environment/Daemons
Provides: bacula-storage = %{version}-%{release}
Requires: bacula-storage-common = %{version}-%{release}
Requires: bacula-common = %{version}-%{release}

%description storage-postgresql
Bacula is a set of programs that allow you to manage the backup,
recovery, and verification of computer data across a network of
different computers. It is based on a client/server architecture.

This package contains the storage daemon, the daemon responsible for 
writing the data received from the clients onto tape drives or other 
mass storage devices.


%package common
Summary: Common Bacula utilities
Group: System Environment/Daemons
#Requires: bacula-sysconfdir = %{version}-%{release}
#Requires(pre): fedora-usermgmt
#Requires(postun): fedora-usermgmt

%description common
Bacula is a set of programs that allow you to manage the backup,
recovery, and verification of computer data across a network of
different computers. It is based on a client/server architecture.


%package console
Summary: Bacula management console
Group: System Environment/Daemons
Requires: bacula-common = %{version}-%{release}

%description console
Bacula is a set of programs that allow you to manage the backup,
recovery, and verification of computer data across a network of
different computers. It is based on a client/server architecture.

This package contains the command-line management console for the bacula 
backup system.


#%%package console-gnome
#Summary: Bacula console for the Gnome desktop environment
#Group: System Environment/Daemons
#Requires: bacula-common = %{version}-%{release}
#Requires: usermode
#
#%%description console-gnome
#Bacula is a set of programs that allow you to manage the backup,
#recovery, and verification of computer data across a network of
#different computers. It is based on a client/server architecture.
#
#This package contains the gnome version of the bacula management console

%package console-bat
Summary: Bacula bat console
Group: System Environment/Daemons
Requires: bacula-common = %{version}-%{release}
Requires: usermode

%description console-bat
Bacula is a set of programs that allow you to manage the backup,
recovery, and verification of computer data across a network of
different computers. It is based on a client/server architecture.

This package contains the bat version of the bacula management console


#%%package console-wxwidgets
#Summary: Bacula console using the wx widgets toolkit
#Group: System Environment/Daemons
#Requires: bacula-common = %{version}-%{release}
#Requires: usermode
#
#%%description console-wxwidgets
#Bacula is a set of programs that allow you to manage the backup,
#recovery, and verification of computer data across a network of
#different computers. It is based on a client/server architecture.
#
#This package contains the wxWidgets version of the bacula management 
#console.


%package traymonitor
Summary: Bacula monitor for the Gnome and KDE system tray
Group: System Environment/Daemons
Requires: bacula-common = %{version}-%{release}

%description traymonitor
Bacula is a set of programs that allow you to manage the backup,
recovery, and verification of computer data across a network of
different computers. It is based on a client/server architecture.

This package contains the Gnome- and KDE-compatible tray monitor to 
monitor your bacula server.


#%package web
#Summary: Bacula Web Interface for monitoring the Backup status
#Group: System Environment/Daemons
#Conflicts: bacula-storage-sqlite
#Requires: php, webserver, php-pear-DB, php-gd, php-Smarty

#%description web
#Bacula is a set of programs that allow you to manage the backup,
#recovery, and verification of computer data across a network of
#different computers. It is based on a client/server architecture.

#This package contains the bacula-web PHP application, which is
#a management level tool for reporting Backup job status.


%package docs
Summary: Bacula documentation
Group: Documentation

%description docs
Bacula is a set of programs that allow you to manage the backup,
recovery, and verification of computer data across a network of
different computers. It is based on a client/server architecture.

This package contains the documentation for most of the bacula-packages.


%prep
%setup -q -c -n bacula-%{version}
%setup -q -a 1 -D -T
#%setup -q -a 2 -D -T
#%setup -q -a 10 -D -T

# Patching and other source preparation
pushd bacula-%{version}
%patch0 -p1
%patch1 -p1
#%patch2 -p1
%patch3 -p1
#%patch4 -p0
#%patch5 -p0
#%patch6 -p0
#%patch7 -p0
#%patch8 -p0
#%patch9 -p0
#%patch11 -p0
#%patch12 -p0
%patch13 -p2 -b .openssl

# Remove execution permissions from files we're packaging as docs later on
find examples -type f | xargs chmod -x
find updatedb -type f | xargs chmod -x
popd

# Remove cvs left-overs
find -name '.cvsignore' | xargs rm -f 

# Fix perms of c files to silent rpmlint
find -type f -name '*.c' | xargs chmod -x 
find -type f -name '*.h' | xargs chmod -x 

# GUI Stuff is postponed for later
#pushd bacula-gui-%{gui_version}
#%patch10 -p0
#popd

# We are building the source several times, each with a different storage backend
mkdir bacula-mysql bacula-postgresql bacula-sqlite

%build
# Shell function to configure and build a Bacula tree
build() {
cp -rl ../bacula-%{version}/* .
export CFLAGS=-I%{_includedir}/ncurses
export CPPFLAGS=-I%{_includedir}/ncurses
%configure \
	--sysconfdir=%{_sysconfdir}/bacula \
	--with-dir-user=bacula \
	--with-dir-group=bacula \
	--with-sd-user=bacula \
	--with-sd-group=bacula \
	--with-fd-user=root \
	--with-fd-group=root \
	--with-dir-password=@@DIR_PASSWORD@@ \
	--with-fd-password=@@FD_PASSWORD@@ \
	--with-sd-password=@@SD_PASSWORD@@ \
	--with-mon-dir-password=@@MON_DIR_PASSWORD@@ \
	--with-mon-fd-password=@@MON_FD_PASSWORD@@ \
	--with-mon-sd-password=@@MON_SD_PASSWORD@@ \
	--with-working-dir=%{working_dir} \
	--with-scriptdir=%{script_dir} \
	--with-smtp-host=localhost \
	--with-subsys-dir=%{_localstatedir}/lock/subsys \
	--with-pid-dir=%{_localstatedir}/run \
	--enable-conio \
	--enable-largefile \
	--enable-tray-monitor \
	--enable-build-dird \
	--enable-build-stored \
	--with-openssl \
	--with-tcp-wrappers \
	--with-python \
	--enable-smartalloc \
	--with-x \
	--enable-bat \
	--with-qwt=/usr/lib \
	--disable-libtool \
	$*
# Scratch this, it is trouble
#	--with-readline \

if test $? != 0; then 
  tail -500 config.log
  : configure failed
  exit 1
fi

%{__make} %{?_smp_mflags}

}				

# Build sqlite director
pushd bacula-sqlite
%if 0%{?fedora}%{?rhel}
	%if 0%{?fedora}
		%if 0%{fedora} >= 5
			%define	sqlite_suffix 3
			build --with-sqlite3
		%else
			build --with-sqlite
		%endif
	%endif
	%if 0%{?rhel}
		%if 0%{rhel} >=  5
			%define	sqlite_suffix 3
			build --with-sqlite3
		%else
			build --with-sqlite
		%endif
	%endif
%else
	echo 'Neither %%{fedora} nor %%{rhel} are defined.'
	echo 'Please call rpmbuild with at least --define "fedora 7" or --define "rhel 5"'
	echo 'depending on your release version you are building on.'
	exit 1
%endif
popd

# Build MySQL director
pushd bacula-mysql
	build --with-mysql
popd

# Build PostgreSQL director
pushd bacula-postgresql
	build --with-postgresql
popd

# Build the docs
pushd bacula-docs-%{docs_version}
 %configure --with-bacula=%{_builddir}/bacula-%{version}/bacula-%{version}
 make
popd

%install
rm -rf %{buildroot}

pushd bacula-sqlite
	make install DESTDIR=%{buildroot}
	mv %{buildroot}%{_sbindir}/bacula-dir  %{buildroot}%{_sbindir}/bacula-dir.sqlite
	mv %{buildroot}%{_sbindir}/dbcheck  %{buildroot}%{_sbindir}/dbcheck.sqlite
	mv %{buildroot}%{_sbindir}/bcopy  %{buildroot}%{_sbindir}/bcopy.sqlite
	mv %{buildroot}%{_sbindir}/bscan  %{buildroot}%{_sbindir}/bscan.sqlite

	for script in create_bacula_database drop_bacula_database drop_bacula_tables \
			grant_bacula_privileges make_bacula_tables make_catalog_backup \
			update_bacula_tables; do
		mv %{buildroot}%{_libexecdir}/bacula/${script} %{buildroot}%{_libexecdir}/bacula/${script}.sqlite
	done
popd

pushd bacula-mysql
	make install DESTDIR=%{buildroot}
	mv %{buildroot}%{_sbindir}/bacula-dir  %{buildroot}%{_sbindir}/bacula-dir.mysql
	mv %{buildroot}%{_sbindir}/dbcheck  %{buildroot}%{_sbindir}/dbcheck.mysql
	mv %{buildroot}%{_sbindir}/bcopy  %{buildroot}%{_sbindir}/bcopy.mysql
	mv %{buildroot}%{_sbindir}/bscan  %{buildroot}%{_sbindir}/bscan.mysql

	for script in create_bacula_database drop_bacula_database drop_bacula_tables \
			grant_bacula_privileges make_bacula_tables make_catalog_backup \
			update_bacula_tables; do
		mv %{buildroot}%{_libexecdir}/bacula/${script} %{buildroot}%{_libexecdir}/bacula/${script}.mysql
	done
popd

pushd bacula-postgresql
	make install DESTDIR=%{buildroot}
	mv %{buildroot}%{_sbindir}/bacula-dir  %{buildroot}%{_sbindir}/bacula-dir.postgresql
	mv %{buildroot}%{_sbindir}/dbcheck  %{buildroot}%{_sbindir}/dbcheck.postgresql
	mv %{buildroot}%{_sbindir}/bcopy  %{buildroot}%{_sbindir}/bcopy.postgresql
	mv %{buildroot}%{_sbindir}/bscan  %{buildroot}%{_sbindir}/bscan.postgresql

	for script in create_bacula_database drop_bacula_database drop_bacula_tables \
			grant_bacula_privileges make_bacula_tables make_catalog_backup \
			update_bacula_tables; do
		mv %{buildroot}%{_libexecdir}/bacula/${script} %{buildroot}%{_libexecdir}/bacula/${script}.postgresql
	done
popd

pushd bacula-docs-%{docs_version}
 # No install target anymore, we'll include the stuff directly in the %%files section
 #	make install DESTDIR=%{buildroot}
popd

# GUI is not being packaged yet
#pushd bacula-gui-%{gui_version}/bacula-web
#	mkdir -p %{buildroot}%{_datadir}/bacula-web
#	cp -r -p * %{buildroot}%{_datadir}/bacula-web
#	for f in ChangeLog CONTACT COPYING README TODO; do
#		rm -f %{buildroot}%{_datadir}/bacula-web/$f
#	done
#	rm -f %{buildroot}%{_datadir}/bacula-web/tsmarty2c.php
#	rm -rf %{buildroot}%{_datadir}/bacula-web/external_packages/smarty
#	mv %{buildroot}%{_datadir}/bacula-web/configs/bacula.conf %{buildroot}%{_sysconfdir}/bacula/bacula-web.conf
#	ln -sf /etc/bacula/bacula-web.conf %{buildroot}%{_datadir}/bacula-web/configs/bacula.conf
#	install -D -m 644 %{SOURCE11} %{buildroot}%{_sysconfdir}/httpd/conf.d/bacula-web.conf
#	mkdir -p %{buildroot}%{_localstatedir}/cache/bacula
#popd


# Rename some manpages
# Not needed right-now
#mv %{buildroot}%{_mandir}/man1/bacula-tray-monitor.1 %{buildroot}%{_mandir}/man1/tray-monitor.1


# Fix some wrapper braindeadness
rm -f %{buildroot}%{_libexecdir}/bacula/bconsole
rm -f %{buildroot}%{_libexecdir}/bacula/gconsole
#mv %{buildroot}%{_sbindir}/bwx-console %{buildroot}%{_sbindir}/bwxconsole
#mv %{buildroot}%{_sysconfdir}/bacula/bwx-console.conf %{buildroot}%{_sysconfdir}/bacula/bwxconsole.conf

# Rename configure output
mv %{buildroot}%{_libexecdir}/bacula/bacula_config %{buildroot}%{_libexecdir}/bacula/bacula_config.%{_arch}

#no wx console (rhbz#564091)
rm -f %{buildroot}%{_mandir}/man1/bacula-bwxconsole.1*

# Desktop Integration for the console apps and the traymonitor
mkdir -p %{buildroot}%{_bindir}
install -m 644 -D bacula-sqlite/scripts/bacula.png %{buildroot}%{_datadir}/pixmaps/bacula.png
#install -m 644 -D bacula-sqlite/scripts/bgnome-console.pamd %{buildroot}%{_sysconfdir}/pam.d/bgnome-console
#install -m 644 -D bacula-sqlite/scripts/bgnome-console.console_apps %{buildroot}%{_sysconfdir}/security/console.apps/bgnome-console
#install -m 644 -D bacula-sqlite/src/wx-console/wxwin16x16.xpm %{buildroot}%{_datadir}/pixmaps/wxwin16x16.xpm
#install -m 644 -D bacula-sqlite/scripts/wxconsole.pamd %{buildroot}%{_sysconfdir}/pam.d/wxconsole
#install -m 644 -D bacula-sqlite/scripts/wxconsole.desktop.consolehelper %{buildroot}%{_sysconfdir}/security/console.apps/wxconsole
#bat.pamd is broken.
install -m 644 -D bacula-sqlite/scripts/bgnome-console.pamd %{buildroot}%{_sysconfdir}/pam.d/bat
install -m 644 -D bacula-sqlite/scripts/bat.console_apps %{buildroot}%{_sysconfdir}/security/console.apps/bat
install -m 644 -D bacula-sqlite/src/tray-monitor/generic.xpm %{buildroot}%{_datadir}/pixmaps/bacula-tray-monitor.xpm
install -m 644 -D bacula-sqlite/src/qt-console/images/bat_icon.png %{buildroot}%{_datadir}/pixmaps/bat_icon.png
install -m 644 -D bacula-sqlite/scripts/bgnome-console.pamd %{buildroot}%{_sysconfdir}/pam.d/bacula-tray-monitor
install -m 644 %{SOURCE13} %{buildroot}%{_sysconfdir}/security/console.apps/bacula-tray-monitor

#ln -sf consolehelper %{buildroot}%{_bindir}/bgnome-console
#ln -sf consolehelper %{buildroot}%{_bindir}/wxconsole
ln -sf consolehelper %{buildroot}%{_bindir}/bat
ln -sf consolehelper %{buildroot}%{_bindir}/bacula-tray-monitor
install -m 755 bacula-sqlite/src/qt-console/bat %{buildroot}%{_sbindir}

#desktop-file-install --vendor="fedora" --dir=%{buildroot}%{_datadir}/applications %{SOURCE3}
#desktop-file-install --vendor="fedora" --dir=%{buildroot}%{_datadir}/applications %{SOURCE4}
desktop-file-install --vendor="fedora" --dir=%{buildroot}%{_datadir}/applications %{SOURCE5}
desktop-file-install --vendor="fedora" --dir=%{buildroot}%{_datadir}/applications %{SOURCE12}


# logrotate
mkdir -p %{buildroot}%{_localstatedir}/log/bacula
install -m 644 -D %{SOURCE6} %{buildroot}%{_sysconfdir}/logrotate.d/bacula


# And logwatch
install -m 755 -D bacula-sqlite/scripts/logwatch/bacula %{buildroot}%{_sysconfdir}/logwatch/scripts/services/bacula
install -m 644 -D bacula-sqlite/scripts/logwatch/logfile.bacula.conf %{buildroot}%{_sysconfdir}/logwatch/conf/logfiles/bacula.conf
install -m 644 -D bacula-sqlite/scripts/logwatch/services.bacula.conf %{buildroot}%{_sysconfdir}/logwatch/conf/services/bacula.conf


# Initscripts
install -m 755 -D %{SOURCE7}  %{buildroot}%{_initrddir}/bacula-fd
install -m 755 -D %{SOURCE8}  %{buildroot}%{_initrddir}/bacula-dir
install -m 755 -D %{SOURCE9}  %{buildroot}%{_initrddir}/bacula-sd


# Wipe backup files from the multiple make install calls
rm -vf %{buildroot}%{_sysconfdir}/bacula/*.{new,old}
rm -vf %{buildroot}%{_libexecdir}/bacula/*.{new,old}


# Create the spooling
mkdir -p %{buildroot}%{_localstatedir}/spool/bacula


# Move some files around
mv %{buildroot}%{_libexecdir}/bacula/query.sql %{buildroot}%{_sysconfdir}/bacula/query.sql


# Nuke the scripts we do not need
rm -vf %{buildroot}%{_libexecdir}/bacula/{bacula,bacula-ctl-*,startmysql,stopmysql} 


# Fix up some perms so rpmlint does not complain too much
chmod 755 %{buildroot}%{_sbindir}/*
chmod 755 %{buildroot}%{_libexecdir}/bacula/*
chmod 644 %{buildroot}%{_libexecdir}/bacula/btraceback.*

# Remove extra docs
rm -rf %{buildroot}%{_datadir}/doc/bacula/

%clean
rm -rf %{buildroot}


%post director-mysql
/usr/sbin/alternatives --install /usr/sbin/bacula-dir bacula-dir /usr/sbin/bacula-dir.mysql 50 \
	--slave /usr/sbin/dbcheck bacula-dbcheck /usr/sbin/dbcheck.mysql \
	--slave /usr/libexec/bacula/create_bacula_database create_bacula_database /usr/libexec/bacula/create_bacula_database.mysql \
	--slave /usr/libexec/bacula/drop_bacula_database drop_bacula_database /usr/libexec/bacula/drop_bacula_database.mysql \
	--slave /usr/libexec/bacula/drop_bacula_tables drop_bacula_tables /usr/libexec/bacula/drop_bacula_tables.mysql \
	--slave /usr/libexec/bacula/grant_bacula_privileges grant_bacula_privileges /usr/libexec/bacula/grant_bacula_privileges.mysql \
	--slave /usr/libexec/bacula/make_bacula_tables make_bacula_tables /usr/libexec/bacula/make_bacula_tables.mysql \
	--slave /usr/libexec/bacula/make_catalog_backup make_catalog_backup /usr/libexec/bacula/make_catalog_backup.mysql \
	--slave /usr/libexec/bacula/update_bacula_tables update_bacula_tables /usr/libexec/bacula/update_bacula_tables.mysql


%post director-sqlite
/usr/sbin/alternatives --install /usr/sbin/bacula-dir bacula-dir /usr/sbin/bacula-dir.sqlite 40 \
	--slave /usr/sbin/dbcheck bacula-dbcheck /usr/sbin/dbcheck.sqlite \
	--slave /usr/libexec/bacula/create_bacula_database create_bacula_database /usr/libexec/bacula/create_bacula_database.sqlite \
	--slave /usr/libexec/bacula/drop_bacula_database drop_bacula_database /usr/libexec/bacula/drop_bacula_database.sqlite \
	--slave /usr/libexec/bacula/drop_bacula_tables drop_bacula_tables /usr/libexec/bacula/drop_bacula_tables.sqlite \
	--slave /usr/libexec/bacula/grant_bacula_privileges grant_bacula_privileges /usr/libexec/bacula/grant_bacula_privileges.sqlite \
	--slave /usr/libexec/bacula/make_bacula_tables make_bacula_tables /usr/libexec/bacula/make_bacula_tables.sqlite \
	--slave /usr/libexec/bacula/make_catalog_backup make_catalog_backup /usr/libexec/bacula/make_catalog_backup.sqlite \
	--slave /usr/libexec/bacula/update_bacula_tables update_bacula_tables /usr/libexec/bacula/update_bacula_tables.sqlite


%post director-postgresql
/usr/sbin/alternatives --install /usr/sbin/bacula-dir bacula-dir /usr/sbin/bacula-dir.postgresql 60 \
	--slave /usr/sbin/dbcheck bacula-dbcheck /usr/sbin/dbcheck.postgresql \
	--slave /usr/libexec/bacula/create_bacula_database create_bacula_database /usr/libexec/bacula/create_bacula_database.postgresql \
	--slave /usr/libexec/bacula/drop_bacula_database drop_bacula_database /usr/libexec/bacula/drop_bacula_database.postgresql \
	--slave /usr/libexec/bacula/drop_bacula_tables drop_bacula_tables /usr/libexec/bacula/drop_bacula_tables.postgresql \
	--slave /usr/libexec/bacula/grant_bacula_privileges grant_bacula_privileges /usr/libexec/bacula/grant_bacula_privileges.postgresql \
	--slave /usr/libexec/bacula/make_bacula_tables make_bacula_tables /usr/libexec/bacula/make_bacula_tables.postgresql \
	--slave /usr/libexec/bacula/make_catalog_backup make_catalog_backup /usr/libexec/bacula/make_catalog_backup.postgresql \
	--slave /usr/libexec/bacula/update_bacula_tables update_bacula_tables /usr/libexec/bacula/update_bacula_tables.postgresql


%preun director-mysql
if [ "$1" = 0 ]; then
	/usr/sbin/alternatives --remove bacula-dir /usr/sbin/bacula-dir.mysql
fi


%preun director-sqlite
if [ "$1" = 0 ]; then
	/usr/sbin/alternatives --remove bacula-dir /usr/sbin/bacula-dir.sqlite
fi


%preun director-postgresql
if [ "$1" = 0 ]; then
	/usr/sbin/alternatives --remove bacula-dir /usr/sbin/bacula-dir.postgresql
fi

%pre common
/usr/sbin/groupadd -g 133 -r bacula &>/dev/null || :
/usr/sbin/useradd  -u 133 -r -s /sbin/nologin -d /var/spool/bacula -M \
	-c 'Bacula Backup System' -g bacula bacula &>/dev/null || :


%postun common
#Dropped due to Guidelines
#test "$1" != 0 || /usr/sbin/userdel  bacula &>/dev/null || :
#test "$1" != 0 || /usr/sbin/groupdel bacula &>/dev/null || :


%post storage-mysql
/usr/sbin/alternatives --install /usr/sbin/bcopy bacula-sd /usr/sbin/bcopy.mysql 50 \
	--slave /usr/sbin/dbcheck bacula-bscan /usr/sbin/bscan.mysql 


%post storage-sqlite
/usr/sbin/alternatives --install /usr/sbin/bcopy bacula-sd /usr/sbin/bcopy.sqlite 40 \
	--slave /usr/sbin/dbcheck bacula-bscan /usr/sbin/bscan.sqlite


%post storage-postgresql
/usr/sbin/alternatives --install /usr/sbin/bcopy bacula-sd /usr/sbin/bcopy.postgresql 60 \
	--slave /usr/sbin/dbcheck bacula-bscan /usr/sbin/bscan.postgresql


%preun storage-mysql
if [ "$1" = 0 ]; then
	/usr/sbin/alternatives --remove bacula-sd /usr/sbin/bcopy.mysql
fi

%preun storage-sqlite
if [ "$1" = 0 ]; then
	/usr/sbin/alternatives --remove bacula-sd /usr/sbin/bcopy.sqlite
fi

%preun storage-postgresql
if [ "$1" = 0 ]; then
	/usr/sbin/alternatives --remove bacula-sd /usr/sbin/bcopy.postgresql
fi

%post client
/sbin/chkconfig --add bacula-fd


%preun client
if [ "$1" = 0 ]; then
	/sbin/service bacula-fd stop >/dev/null 2>&1 || :
	/sbin/chkconfig --del bacula-fd
fi


%postun client
if [ "$1" -ge "1" ]; then
	/sbin/service bacula-fd condrestart >/dev/null 2>&1 || :
fi


%post director-common
/sbin/chkconfig --add bacula-dir


%preun director-common
if [ "$1" = 0 ]; then
	/sbin/service bacula-dir stop >/dev/null 2>&1 || :
	/sbin/chkconfig --del bacula-dir
fi


%postun director-common
if [ "$1" -ge "1" ]; then
	/sbin/service bacula-dir condrestart >/dev/null 2>&1 || :
fi


%post storage-common
/sbin/chkconfig --add bacula-sd


%preun storage-common
if [ "$1" = 0 ]; then
	/sbin/service bacula-sd stop >/dev/null 2>&1 || :
	/sbin/chkconfig --del bacula-sd
fi


%postun storage-common
if [ "$1" -ge "1" ]; then
	/sbin/service bacula-sd condrestart >/dev/null 2>&1 || :
fi




%files common
%defattr(-,root,root,-)
%doc bacula-%{version}/AUTHORS bacula-%{version}/ChangeLog bacula-%{version}/COPYING bacula-%{version}/LICENSE
%doc bacula-%{version}/README bacula-%{version}/SUPPORT bacula-%{version}/VERIFYING
%doc bacula-%{version}/examples/
%config(noreplace) %{_sysconfdir}/logrotate.d/bacula
%dir %{_libexecdir}/bacula
%dir %{_sysconfdir}/bacula
%{_sbindir}/bsmtp
%{_sbindir}/btraceback
%{_libexecdir}/bacula/btraceback.dbx
%{_libexecdir}/bacula/btraceback.gdb
%{_mandir}/man1/bsmtp.1*
%{_mandir}/man8/bacula.8*
%{_mandir}/man8/btraceback.8*
%dir %attr(750, bacula, bacula) %{_localstatedir}/log/bacula
%dir %attr(750, bacula, bacula) %{_localstatedir}/spool/bacula
%{_sbindir}/bacula
#%%{_libdir}/bpipe-fd.so
/usr/libexec/bacula/mtx-changer.conf
%{_libexecdir}/bacula/bacula_config.%{_arch}

%files client
%defattr(-,root,root,-)
%{_sbindir}/bacula-fd
%{_initrddir}/bacula-fd
%config(noreplace) %{_sysconfdir}/bacula/bacula-fd.conf
%{_mandir}/man8/bacula-fd.8*


%files console
%defattr(-,root,root,-)
%{_sbindir}/bconsole
%attr(640,root,bacula) %config(noreplace) %{_sysconfdir}/bacula/bconsole.conf
%{_mandir}/man8/bconsole.8*



%files console-bat
%defattr(-,root,root,-)
%config %{_sysconfdir}/security/console.apps/bat
%config %{_sysconfdir}/pam.d/bat
%attr(640,root,bacula) %config(noreplace) %{_sysconfdir}/bacula/bat.conf
%{_bindir}/bat
%{_sbindir}/bat
%{_mandir}/man1/bat.1.gz
%{_datadir}/applications/fedora-bacula-bat.desktop
%{_datadir}/pixmaps/bat_icon.png
%{_datadir}/pixmaps/bacula.png



%files director-common
%defattr(-,root,root,-)
%doc bacula-%{version}/updatedb/
%config(noreplace) %{_sysconfdir}/bacula/bacula-dir.conf
%config(noreplace) %{_sysconfdir}/bacula/query.sql
%config %{_sysconfdir}/logwatch/conf/logfiles/bacula.conf
%config %{_sysconfdir}/logwatch/conf/services/bacula.conf
%{_sysconfdir}/logwatch/scripts/services/bacula
%{_initrddir}/bacula-dir
%{_sbindir}/bregex
%{_sbindir}/bwild
%{_mandir}/man8/dbcheck.8*
%{_mandir}/man8/bacula-dir.8*
%{_libexecdir}/bacula/delete_catalog_backup
%{_libexecdir}/bacula/make_catalog_backup.pl


%files director-mysql
%defattr(-,root,root,-)
%{_sbindir}/bacula-dir.mysql
%{_sbindir}/dbcheck.mysql
%{_libexecdir}/bacula/create_mysql_database
%{_libexecdir}/bacula/drop_mysql_database
%{_libexecdir}/bacula/drop_mysql_tables
%{_libexecdir}/bacula/grant_mysql_privileges
%{_libexecdir}/bacula/make_mysql_tables
%{_libexecdir}/bacula/update_mysql_tables
%{_libexecdir}/bacula/create_bacula_database.mysql
%{_libexecdir}/bacula/drop_bacula_database.mysql
%{_libexecdir}/bacula/drop_bacula_tables.mysql
%{_libexecdir}/bacula/grant_bacula_privileges.mysql
%{_libexecdir}/bacula/make_bacula_tables.mysql
%{_libexecdir}/bacula/make_catalog_backup.mysql
%{_libexecdir}/bacula/update_bacula_tables.mysql



%files director-sqlite
%defattr(-,root,root,-)
%{_sbindir}/bacula-dir.sqlite
%{_sbindir}/dbcheck.sqlite
# DANGER Will Robinson. Bacula has versioned sqlite filenames
%{_libexecdir}/bacula/create_sqlite%{?sqlite_suffix}_database
%{_libexecdir}/bacula/drop_sqlite%{?sqlite_suffix}_database
%{_libexecdir}/bacula/drop_sqlite%{?sqlite_suffix}_tables
%{_libexecdir}/bacula/grant_sqlite%{?sqlite_suffix}_privileges
%{_libexecdir}/bacula/make_sqlite%{?sqlite_suffix}_tables
%{_libexecdir}/bacula/update_sqlite%{?sqlite_suffix}_tables
%{_libexecdir}/bacula/create_bacula_database.sqlite
%{_libexecdir}/bacula/drop_bacula_database.sqlite
%{_libexecdir}/bacula/drop_bacula_tables.sqlite
%{_libexecdir}/bacula/grant_bacula_privileges.sqlite
%{_libexecdir}/bacula/make_bacula_tables.sqlite
%{_libexecdir}/bacula/make_catalog_backup.sqlite
%{_libexecdir}/bacula/update_bacula_tables.sqlite


%files director-postgresql
%defattr(-,root,root,-)
%{_sbindir}/bacula-dir.postgresql
%{_sbindir}/dbcheck.postgresql
%{_libexecdir}/bacula/create_postgresql_database
%{_libexecdir}/bacula/drop_postgresql_database
%{_libexecdir}/bacula/drop_postgresql_tables
%{_libexecdir}/bacula/grant_postgresql_privileges
%{_libexecdir}/bacula/make_postgresql_tables
%{_libexecdir}/bacula/update_postgresql_tables
%{_libexecdir}/bacula/create_bacula_database.postgresql
%{_libexecdir}/bacula/drop_bacula_database.postgresql
%{_libexecdir}/bacula/drop_bacula_tables.postgresql
%{_libexecdir}/bacula/grant_bacula_privileges.postgresql
%{_libexecdir}/bacula/make_bacula_tables.postgresql
%{_libexecdir}/bacula/make_catalog_backup.postgresql
%{_libexecdir}/bacula/update_bacula_tables.postgresql


%files storage-common
%defattr(-,root,root,-)
%{_sbindir}/bacula-sd
%{_sbindir}/bextract
%{_sbindir}/bls
%{_sbindir}/btape
%config(noreplace) %{_sysconfdir}/bacula/bacula-sd.conf
%{_initrddir}/bacula-sd
%{_libexecdir}/bacula/disk-changer
%{_libexecdir}/bacula/dvd-handler
%{_libexecdir}/bacula/mtx-changer
%{_mandir}/man8/bcopy.8*
%{_mandir}/man8/bextract.8*
%{_mandir}/man8/bls.8*
%{_mandir}/man8/bscan.8*
%{_mandir}/man8/btape.8*
%{_mandir}/man8/bacula-sd.8*


%files storage-mysql
%defattr(-,root,root,-)
%{_sbindir}/bcopy.mysql
%{_sbindir}/bscan.mysql


%files storage-sqlite
%defattr(-,root,root,-)
%{_sbindir}/bcopy.sqlite
%{_sbindir}/bscan.sqlite


%files storage-postgresql
%defattr(-,root,root,-)
%{_sbindir}/bcopy.postgresql
%{_sbindir}/bscan.postgresql


%files traymonitor
%defattr(-,root,root,-)
%{_bindir}/bacula-tray-monitor
%{_sbindir}/bacula-tray-monitor
%attr(640,root,bacula) %config(noreplace) %{_sysconfdir}/bacula/tray-monitor.conf
%config %{_sysconfdir}/security/console.apps/bacula-tray-monitor
%config %{_sysconfdir}/pam.d/bacula-tray-monitor
%{_mandir}/man1/bacula-tray-monitor.1*
%{_datadir}/applications/fedora-bacula-traymonitor.desktop
%{_datadir}/pixmaps/bacula-tray-monitor.xpm


%files docs
%defattr(-,root,root,-)
#%%doc bacula-docs-%{docs_version}/manuals/en/install/install.pdf
%doc bacula-docs-%{docs_version}/manuals/en/problems/problems.pdf
%doc bacula-docs-%{docs_version}/manuals/en/console/console.pdf
%doc bacula-docs-%{docs_version}/manuals/en/utility/utility.pdf
#%%doc bacula-docs-%{docs_version}/manuals/en/concepts/concepts.pdf
#%%doc bacula-docs-%{docs_version}/manuals/en/catalog/catalog.pdf
%doc bacula-docs-%{docs_version}/manuals/en/developers/developers.pdf
%doc bacula-docs-%{docs_version}/manuals/en/main/main.pdf
%doc bacula-docs-%{docs_version}/manuals/en/misc/misc.pdf

#%files web
#%defattr(-,root,root,-)
#%doc bacula-gui-%{gui_version}/bacula-web/CONTACT bacula-gui-%{gui_version}/bacula-web/COPYING
#%doc bacula-gui-%{gui_version}/bacula-web/README bacula-gui-%{gui_version}/bacula-web/TODO
#%{_datadir}/bacula-web/
#%config(noreplace) %{_sysconfdir}/bacula/bacula-web.conf
#%config(noreplace) %{_sysconfdir}/httpd/conf.d/bacula-web.conf
#%dir %attr(755, apache, apache) %{_localstatedir}/cache/bacula-web


%changelog
* Tue Jun 22 2010 Jan Görig <jgorig@redhat.com> 5.0.0-7
- fixed multilib issue (#594115)
- removed hostnames from bconsole.config (#603052)
- fixed desktop files (#603061)
- unconfigured service now returns correct return code

* Tue May 25 2010 Jan Görig <jgorig@redhat.com> 5.0.0-6
- initscripts improvements
- fixed consolehelper settings and menu entries
- Resolves: rhbz#587254 rhbz#587924

* Wed Apr 07 2010 Daniel Novotny <dnovotny@redhat.com> 5.0.0-5
- removed wxGTK BuildRequires (#564091)

* Wed Mar 31 2010 Daniel Novotny <dnovotny@redhat.com> 5.0.0-4
- removed wxWidgets version of the administration frontend (#564091)
  please use bacula-console-bat instead

* Tue Mar 23 2010 Daniel Novotny <dnovotny@redhat.com> 5.0.0-3
- corrected parameters of useradd(8) and groupadd(8) (#574378)

* Wed Mar 17 2010 Daniel Novotny <dnovotny@redhat.com> 5.0.0-2
- subpackage -sysconfdir merged with -common (#574378)

* Wed Mar 03 2010 Daniel Novotny <dnovotny@redhat.com> 5.0.0-1
- rebase to 5.0.0

* Fri Jan 15 2010 Daniel Novotny <dnovotny@redhat.com> 3.0.2-8
- fix #530573 -  Typo in %%postun scriptlet

* Tue Jan 12 2010 Daniel Novotny <dnovotny@redhat.com> 3.0.2-7
- the reserved UID and GID is agreed to be 133 (#554705)

* Tue Jan 12 2010 Daniel Novotny <dnovotny@redhat.com> 3.0.2-6
- fix #554407 -  drop requirement on fedora-usermgmt

* Mon Jan 11 2010 Daniel Novotny <dnovotny@redhat.com> 3.0.2-5
- fix source URL

* Fri Nov 13 2009 Dennis Gregorovic <dgregor@redhat.com> - 3.0.2-4.1
- Fix conditional for RHEL

* Sat Aug 22 2009 Tomas Mraz <tmraz@redhat.com> - 3.0.2-4
- rebuilt with new openssl

* Mon Aug 10 2009 Jon Ciesla <limb@jcomserv.net - 3.0.2-3
- Dropped user/group removal per guidelines.
- Added -common dep to traymonitor.

* Thu Jul 30 2009 Jon Ciesla <limb@jcomserv.net - 3.0.2-2
- gnome-console consolehelper correction. BZ 426790.
- add tray-monitor to consolehelper. BZ 426790

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Jon Ciesla <limb@jcomserv.net - 3.0.2-0
- Update to new upstream, 3.0.2.
- Put full paths in desktop files. BZ 426790.
- Moved console requires from sysconfdir to common BZ 505755.

* Thu Apr 30 2009 Jon Ciesla <limb@jcomserv.net - 3.0.1-1
- Update to new upstream, 3.0.1.

* Tue Apr 21 2009 Jon Ciesla <limb@jcomserv.net - 3.0.0-1
- Update to new upstream, 3.0.0.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 23 2009 Jon Ciesla <limb@jcomserv.net - 2.4.4-2
- Rebuild against mysql 5.1.

* Mon Jan 05 2009 Jon Ciesla <limb@jcomserv.net - 2.4.4-1
- Update to new upstream, 2.4.4.
- Dropped orphaned jobs patch, python 2.6 patch, applied upstream.

* Mon Dec 15 2008 Jon Ciesla <limb@jcomserv.net - 2.4.3-7
- Patched to support Python 2.6, BZ 476547.

* Fri Dec 12 2008 Jon Ciesla <limb@jcomserv.net - 2.4.3-6
- Fix consolehelper behaviour for bat.

* Wed Dec 10 2008 Jon Ciesla <limb@jcomserv.net - 2.4.3-5
- Re-diffed fuzzy bacula-director-configuration and bacula-config patches.

* Mon Dec 1 2008 Andreas Thienemann <andreas@bawue.net> - 2.4.3-4
- Fixed dependency "issues" #473627 by adding the sysconfdir subpackage.

* Mon Nov 17 2008 Jon Ciesla <limb@jcomserv.net> - 2.4.3-3
- Added upstream orphaned jobs patch.
- Fixed logrotate file.

* Mon Nov 10 2008 Jon Ciesla <limb@jcomserv.net> - 2.4.3-2
- Added bat.  BZ 470800.

* Wed Oct 22 2008 Jon Ciesla <limb@jcomserv.net> - 2.4.3-1
- Update to 2.4.3.

* Tue Sep 09 2008 Jon Ciesla <limb@jcomserv.net> - 2.4.2-2
- Logrotate fix. BZ 457894.
- Alternatives fix. BZ 458432.

* Thu Jul 31 2008 Jon Ciesla <limb@jcomserv.net> - 2.4.2-1
- Update to 2.4.2.

* Wed Jul 30 2008 Andreas Thienemann <athienem@redhat.com> - 2.2.8-2
- Fixed %%{fedora} comparision, making bacula-sqlite build on rawhide

* Fri Jul 25 2008 Jon Ciesla <limb@jcomserv.net> - 2.2.8-1
- Update to 2.2.8. BZ 446461.
- Dropped director and storage DB-server hard Reqs. BZ 426788.
- .desktop fixes.  BZ 450278, 426789.
- Updated config patch.
- Dropped wxconsole patch, applied upstream.
- Updated pamd patch.
- Dropped ampm patch, applied upstream.
- Dropped maxbyteslist patch, N/A.
- Dropped maxwaittime patch, applied upstream.
- Dropped scheduler-next-hour patch, applied upstream.
- Dropped verify patch, applied upstream.
- Dropped tls-disconnect patch, applied upstream.
- Fix for 426791.
- Introduced patch fuzz workaround, will fix.

* Mon Jul  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.3-14
- fix conditional comparison
- fix license tag

* Mon Jan 07 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.3-13
- add BR: dvipdfm

* Thu Dec 06 2007 Release Engineering <rel-eng at fedoraproject dot org> - 2.0.3-12
 - Rebuild for deps

* Wed Sep 5 2007 Andreas Thienemann <andreas@bawue.net> - 2.0.3-11
- Remove spooldir in client, fixing #251879
- Remove dependency on libtermcap, fixing #251158

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 2.0.3-10
- Rebuild for selinux ppc32 issue.

* Wed Jul 25 2007 Andreas Thienemann <andreas@bawue.net> 2.0.3-9
- Corrected the %%post alternatives calls. Fixing #249560.

* Wed Jul 19 2007 Andreas Thienemann <andreas@bawue.net> 2.0.3-8
- Moved some files around in the %%files section and refactored
  spec parts a bit
- Fixed up the catalog-backup scripts by including them in the
  alternatives system
- Applied tls patch fixing some tls disconnection issues.

* Thu Jul 18 2007 Andreas Thienemann <andreas@bawue.net> 2.0.3-7
- Minor specchanges, mostly typos in the comments
- Incorporated minor changes from dgilmore's review.

* Fri Jul 13 2007 Andreas Thienemann <andreas@bawue.net> 2.0.3-6
- Fixing %%preun scripts. Thx to Dan for spotting this

* Fri Jul 13 2007 Andreas Thienemann <andreas@bawue.net> 2.0.3-5
- Fixed provides and requires

* Wed Jul 11 2007 Andreas Thienemann <andreas@bawue.net> 2.0.3-4
- Fixed many rpmlint issues

* Thu Apr 26 2007 Andreas Thienemann <andreas@bawue.net> 2.0.3-3
- Final cleanups for fedora
- Removed webgui for now. It will be back in a future release
- Added LANG=C calls to the initscripts

* Thu Apr 26 2007 Andreas Thienemann <andreas@bawue.net> 2.0.3-2
- Added logdir
- Fixed up doc-creation to actually work
- Fixed up web interface
- Included docs sub-package
- Included README et al as docs where appropriate

* Sat Mar 10 2007 Andreas Thienemann <andreas@bawue.net> 2.0.3-1
- Updated to 2.0.3
- Reverted the database-check as we're not sure the db is running on the
  local machine. A later revision might parse the bacula-dir.conf file
  and just connect to the db to see if it's running.

* Sat Feb 28 2007 Andreas Thienemann <andreas@bawue.net> 2.0.2-1
- Further updates on the spec

* Sat Feb 18 2007 Andreas Thienemann <andreas@bawue.net> 2.0.2-1
- Much work on the spec
- Updated to 2.0.2

* Sat Feb 18 2006 Andreas Thienemann <andreas@bawue.net> 1.38.11-1
- Initial spec.
