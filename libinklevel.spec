##### GENERAL STUFF #####

%define libname %mklibname inklevel 4
%define develname %mklibname -d inklevel
%define old_libname %mklibname inklevel 2

Summary:	Library to determine the ink levels of HP and Epson inkjets
Name:		libinklevel
Version:	0.7.3
Release:	%mkrel 2
License:	GPLv2
Group:		Publishing
Url:		http://libinklevel.sourceforge.net/

##### SOURCE FILES #####

Source: http://heanet.dl.sourceforge.net/sourceforge/libinklevel/libinklevel-%{version}.tar.gz

##### ADDITIONAL DEFINITIONS #####

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
Obsoletes:	%old_libname

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
Obsoletes:	%{old_libname}-devel
Group:		Development/C

%description -n %{develname}
This package contains all files which one needs to compile programs using
the "%{libname}" library.


##### PREP #####

%prep
%setup -q
sed -i -e 's|$(PREFIX)/lib|$(PREFIX)/%{_lib}|' Makefile

##### BUILD #####

%build
%make CFLAGS="%{optflags} -fPIC"

##### INSTALL #####

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix}

##### PRE/POST INSTALL SCRIPTS #####

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT


##### FILE LISTS FOR ALL BINARY PACKAGES #####

##### libinklevel
%files -n %libname
%defattr(-,root,root)
%doc CHANGELOG AUTHORS
%{_libdir}/*.so.*

##### libinklevel-devel
%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/*

##### CHANGELOG #####

