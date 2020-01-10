Summary: Script to enable serial console in all the right places.
Name: SL_enable_serialconsole 
Version: 4.0
Release: 1
Group: SL
License: GPL
Vendor: Scientific Linux
Packager: Steven Timm <timm@fnal.gov>
#modification in packaging by Connie Sieh <csieh@fnal.gov>
#3.1 Release 4 changes to agetty instead of mingetty S. Timm 1/6/06
#3.1 Release 5 beats ttyS1 vs ttyS0 bug S. Timm 5/16/06
Source: serialconsole_all.pl
requires : perl initscripts
BuildRoot: /var/tmp/serialconsole-build
BuildArch: noarch

# Defaults to /dev/ttyS0 with a speed of 9600
%description
This package will install (and automatically run) the 'serialconsole'
script.  This script makes all the changes necessary to send
console output to both the serial port and the screen.  This
also creates a login prompt on the serial port and allows root
to login at this prompt.  This rpm should be installed in the %post 
section because it requires the grub.conf file to be there.
This package only works with grub.

%package 96
Summary: enable serial console for 9600 baud
Group: SL

%description 96
This package will install (and automatically run) the 'serialconsole'
script.  This script makes all the changes necessary to send
console output to both the serial port and the screen.  This
also creates a login prompt on the serial port and allows root
to login at this prompt.  This rpm should be installed in the %post 
section because it requires the grub.conf file to be there.
This package only works with grub.


%package 192
Summary: enable serial console for 19200 baud
Group: SL

%description 192
This package will install (and automatically run) the 'serialconsole'
script.  This script makes all the changes necessary to send
console output to both the serial port and the screen.  This
also creates a login prompt on the serial port and allows root
to login at this prompt.  This rpm should be installed in the %post 
section because it requires the grub.conf file to be there.
This package only works with grub.


%package 384
Summary: enable serial console for 38400  baud
Group: SL 

%description 384
This package will install (and automatically run) the 'serialconsole'
script.  This script makes all the changes necessary to send
console output to both the serial port and the screen.  This
also creates a login prompt on the serial port and allows root
to login at this prompt.  This rpm should be installed in the %post 
section because it requires the grub.conf file to be there.
This package only works with grub.


%package 1152
Summary: enable serial console for 38400  baud
Group: SL 

%description 1152
This package will install (and automatically run) the 'serialconsole'
script.  This script makes all the changes necessary to send
console output to both the serial port and the screen.  This
also creates a login prompt on the serial port and allows root
to login at this prompt.  This rpm should be installed in the %post 
section because it requires the grub.conf file to be there.
This package only works with grub.


%prep

%build

%install
cd ${RPM_SOURCE_DIR}
mkdir -p ${RPM_BUILD_ROOT}/usr/sbin
install -m 0700 serialconsole_all.pl ${RPM_BUILD_ROOT}/usr/sbin/serialconsole_all

%clean
rm -rf $RPM_BUILD_ROOT

%post
# Run the script
# Defaults to /dev/ttyS0 with a speed of 9600
/usr/sbin/serialconsole_all 

%files
%attr(-,root,root) /usr/sbin/serialconsole_all

%post 96
# Run the script
/usr/sbin/serialconsole_all -d /dev/ttyS0 -s 9600

%files 96
%attr(-,root,root) /usr/sbin/serialconsole_all

%post 192
# Run the script
/usr/sbin/serialconsole_all -d /dev/ttyS0 -s 19200

%files 192
%attr(-,root,root) /usr/sbin/serialconsole_all

%post 384
# Run the script
/usr/sbin/serialconsole_all -d /dev/ttyS0 -s 38400

%files 384
%attr(-,root,root) /usr/sbin/serialconsole_all

%post 1152
# Run the script
/usr/sbin/serialconsole_all -d /dev/ttyS0 -s 115200

%files 1152
%attr(-,root,root) /usr/sbin/serialconsole_all

%changelog
* Mon Aug 23 2010 Troy Dawson <dawson@fnal.gov> 4.0-1
- Changed the script to only work with grub, not lilo or efi
- For Fedora 13, RHEL 6 (or it's derivatives) or newer due to 
  the startup changes in 

