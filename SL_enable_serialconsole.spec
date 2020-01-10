Name:		SL_enable_serialconsole
Version:	4.1
Release:	1%{?dist}
Summary:	Script to enable serial console in all the right places.
Vendor:		Scientific Linux
Packager:	Pat Riehecky

Group:		SL
License:	GPL
URL:		http://www.scientificlinux.org/
Source0:	SL_enable_serialconsole.tar.gz
BuildArch:	noarch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	bash augeas
Requires:	bash augeas initscripts coreutils sed grub

# Only one at a time
Conflicts:	SL_enable_serialconsole-96
Conflicts:	SL_enable_serialconsole-192
Conflicts:	SL_enable_serialconsole-384
Conflicts:	SL_enable_serialconsole-1152

%description
This package will install (and automatically run) the 'serialconsole' script. This script makes all the changes necessary to send console output to both the serial port and the screen. This also creates a login prompt on the serial port and allows root to login at this prompt.

This package only works with grub.
You can only have one SL_enable_serialconsole installed at a time.  Having extras will cause unknown behavior, as will switching between them with one command.  To change versions fully remove one package then install the other.

%package 96
Summary:	Script to enable serial console in all the right places.
Group:		SL
Requires:	bash augeas initscripts coreutils sed grub
Conflicts:	SL_enable_serialconsole
Conflicts:	SL_enable_serialconsole-192
Conflicts:	SL_enable_serialconsole-384
Conflicts:	SL_enable_serialconsole-1152
%description 96
This package will install (and automatically run) the 'serialconsole' script. This script makes all the changes necessary to send console output to both the serial port and the screen. This also creates a login prompt on the serial port and allows root to login at this prompt.

This package only works with grub.
You can only have one SL_enable_serialconsole installed at a time.  Having extras will cause unknown behavior, as will switching between them with one command.  To change versions fully remove one package then install the other.

%package 192
Summary:	Script to enable serial console in all the right places.
Group:		SL
Requires:	bash augeas initscripts coreutils sed grub
Conflicts:	SL_enable_serialconsole
Conflicts:	SL_enable_serialconsole-96
Conflicts:	SL_enable_serialconsole-384
Conflicts:	SL_enable_serialconsole-1152
%description 192
This package will install (and automatically run) the 'serialconsole' script. This script makes all the changes necessary to send console output to both the serial port and the screen. This also creates a login prompt on the serial port and allows root to login at this prompt.

This package only works with grub.
You can only have one SL_enable_serialconsole installed at a time.  Having extras will cause unknown behavior, as will switching between them with one command.  To change versions fully remove one package then install the other.

%package 384
Summary:	Script to enable serial console in all the right places.
Group:		SL
Requires:	bash augeas initscripts coreutils sed grub
Conflicts:	SL_enable_serialconsole
Conflicts:	SL_enable_serialconsole-96
Conflicts:	SL_enable_serialconsole-192
Conflicts:	SL_enable_serialconsole-1152
%description 384
This package will install (and automatically run) the 'serialconsole' script. This script makes all the changes necessary to send console output to both the serial port and the screen. This also creates a login prompt on the serial port and allows root to login at this prompt.

This package only works with grub.
You can only have one SL_enable_serialconsole installed at a time.  Having extras will cause unknown behavior, as will switching between them with one command.  To change versions fully remove one package then install the other.

%package 1152
Summary:	Script to enable serial console in all the right places.
Group:		SL
Requires:	bash augeas initscripts coreutils sed grub
Conflicts:	SL_enable_serialconsole
Conflicts:	SL_enable_serialconsole-96
Conflicts:	SL_enable_serialconsole-192
Conflicts:	SL_enable_serialconsole-384
%description 1152
This package will install (and automatically run) the 'serialconsole' script. This script makes all the changes necessary to send console output to both the serial port and the screen. This also creates a login prompt on the serial port and allows root to login at this prompt.

This package only works with grub.
You can only have one SL_enable_serialconsole installed at a time.  Having extras will cause unknown behavior, as will switching between them with one command.  To change versions fully remove one package then install the other.

%prep
%setup -q -n SL_enable_serialconsole

%build
bash -n serialconsole_all
if [[ $? -ne 0 ]]; then
    echo "ERROR in script"
    exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/sbin
install -m 0700 serialconsole_all ${RPM_BUILD_ROOT}/usr/sbin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/sbin/serialconsole_all
%doc OLDSCRIPT
%doc README

%post
# Run the script defaults to /dev/ttyS0 with a speed of 9600
/usr/sbin/serialconsole_all

%preun
# Remove the serial configuration as we remove the RPM
if [[ "$1" == '0' ]]; then # uninstall
    /usr/sbin/serialconsole_all -r
fi

%files 96
%defattr(-,root,root,-)
/usr/sbin/serialconsole_all
%doc OLDSCRIPT
%doc README

%post 96
# Run the script for dev/ttyS0 with a speed of 9600
/usr/sbin/serialconsole_all -s 9600

%preun 96
# Remove the serial configuration as we remove the RPM
if [[ "$1" == '0' ]]; then # uninstall
    /usr/sbin/serialconsole_all -r
fi

%files 192
%defattr(-,root,root,-)
/usr/sbin/serialconsole_all
%doc OLDSCRIPT
%doc README

%post 192
# Run the script for /dev/ttyS0 with a speed of 19200
/usr/sbin/serialconsole_all -s 19200

%preun 192
# Remove the serial configuration as we remove the RPM
if [[ "$1" == '0' ]]; then # uninstall
    /usr/sbin/serialconsole_all -r
fi

%files 384
%defattr(-,root,root,-)
/usr/sbin/serialconsole_all
%doc OLDSCRIPT
%doc README

%post 384
# Run the script for /dev/ttyS0 with a speed of 38400
/usr/sbin/serialconsole_all -s 38400

%preun 384
# Remove the serial configuration as we remove the RPM
if [[ "$1" == '0' ]]; then # uninstall
    /usr/sbin/serialconsole_all -r
fi

%files 1152
%defattr(-,root,root,-)
/usr/sbin/serialconsole_all
%doc OLDSCRIPT
%doc README

%post 1152
# Run the script for /dev/ttyS0 with a speed of 115200
/usr/sbin/serialconsole_all -s 115200

%preun 1152
# Remove the serial configuration as we remove the RPM
if [[ "$1" == '0' ]]; then # uninstall
    /usr/sbin/serialconsole_all -r
fi

%changelog
* Mon Jan 30 2012 Pat Riehecky <riehecky@fnal.gov> 4.1-1
- added '-r' option to script for removal of the configuration
- now removes configuration when uninstalled
- Switched to augeas based configuration
- The old script can be found in the %doc folder
- removed support for non-grub bootloaders as none are avalible for SL6
- a number of SPEC file changes to make things cleaner

* Mon Aug 23 2010 Troy Dawson <dawson@fnal.gov> 4.0-1
- Changed the script to only work with grub, not lilo or efi
- For Fedora 13, RHEL 6 (or it's derivatives) or newer due to
  the startup changes in

