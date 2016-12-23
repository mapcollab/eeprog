Summary: eeprog is a Linux C program that allows you to read and write to 24Cxx EEPROM.
Name: eeprog
Version: 0.7.6
Release: 1
Group: System Environment/Daemons
URL: http://www.codesink.org/eeprog.html
Vendor: Codesink
License: GPLv3
Packager: Builder <builder@thales-ktw.site>
Source: %{name}-%{version}.tar.gz


%description
eeprog is a Linux C program that allows you to read and write to 24Cxx EEPROM.
24Cxx EEPROM use the I2C protocol but most common controllers found in most PC hardware only support SMBus (a superset of I2C).
What eeprog does is using SMBus commands to read/write to I2C EEPROM so almost every controller could be used.

%prep
%setup -q -n %{name}-%{version}

%build
make

%install
mkdir -p %{buildroot}/%{_bindir}
install -m755 eeprog %{buildroot}/%{_bindir}

%files
%attr(0755,root,root) %{_bindir}/*

%changelog
* Fri Dec 23 2016 Michal Gawlik <michal.gawlik@thalesgroup.com> 0.7.6-1
- new package built with tito

