##### GENERAL STUFF #####

%define libname %mklibname inklevel 4
%define develname %mklibname -d inklevel

Summary:	Library to determine the ink levels of HP and Epson inkjets
Name:		libinklevel
Version:	0.7.1
Release:	%mkrel 1
License:	GPL
Group:		Publishing
Url:		http://libinklevel.sourceforge.net/

##### SOURCE FILES #####

Source: http://heanet.dl.sourceforge.net/sourceforge/libinklevel/libinklevel-%{version}.tar.gz
Patch0: libinklevel-0.7.1-Makefile.patch

##### ADDITIONAL DEFINITIONS #####

Provides:	libinklevel
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libieee1284-devel

##### SUB-PACKAGES #####

%description

libinklevel is a library for checking the ink level of your printer on
a system which runs Linux. It supports printers attached via parallel
port or usb.

Most current HP inkjets and several Epson inkjets are supported.

%package -n %libname
Summary:	Library to determine the ink levels of HP and Epson inkjets
Provides:	libinklevel
Group:		Publishing

%description -n %libname

libinklevel is a library for checking the ink level of your printer on
a system which runs Linux. It supports printers attached via parallel
port or usb.

Most current HP inkjets and several Epson inkjets are supported.

%package -n %{develname}
Summary: 	Headers and links to compile against the "%{libname}" library
Requires: 	%{libname} = %{version}
Provides:	libinklevel-devel = %{version}-%{release}
Obsoletes:	%{libname}-devel
Group:		Development/C

%description -n %{develname}
This package contains all files which one needs to compile programs using
the "%{libname}" library.


##### PREP #####

%prep
%setup -q
%patch0 -p0

##### BUILD #####

%build
%make

##### INSTALL #####

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT%{_prefix}

##### PRE/POST INSTALL SCRIPTS #####

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT


##### FILE LISTS FOR ALL BINARY PACKAGES #####

##### libinklevel
%files -n %libname
%defattr(-,root,root)
%doc COPYING README
%{_libdir}/*.so.*

##### libinklevel-devel
%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/*

##### CHANGELOG #####

