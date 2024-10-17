##### GENERAL STUFF #####
%define major 5
%define libname %mklibname inklevel %major
%define develname %mklibname -d inklevel
%define old_libname %mklibname inklevel 2
%define beta %nil

Summary:	Library to determine the ink levels of HP and Epson inkjets
Name:		libinklevel
Version:	0.8.0
Release:	4
License:	GPLv2
Group:		Publishing
Url:		https://libinklevel.sourceforge.net/

##### SOURCE FILES #####

Source: http://heanet.dl.sourceforge.net/sourceforge/libinklevel/libinklevel-%{version}%{beta}.tar.gz

##### ADDITIONAL DEFINITIONS #####

BuildRequires:	ieee1284-devel
BuildRequires:	makedepend

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
%setup -q -n %name-%{version}%{beta}

##### BUILD #####

%build
%configure2_5x
%make CFLAGS="%{optflags} -fPIC"

##### INSTALL #####

%install
rm -rf %{buildroot}
%makeinstall_std 
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/*.a
rm -rf %{buildroot}%{_docdir}

##### PRE/POST INSTALL SCRIPTS #####

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}


##### FILE LISTS FOR ALL BINARY PACKAGES #####

##### libinklevel
%files -n %libname
%defattr(-,root,root)
%doc ChangeLog NEWS AUTHORS
%{_libdir}/*.so.%{major}*

##### libinklevel-devel
%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/*

##### CHANGELOG #####



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.0-2mdv2011.0
+ Revision: 620143
- the mass rebuild of 2010.0 packages

* Thu Jun 11 2009 Frederik Himpe <fhimpe@mandriva.org> 0.8.0-1mdv2010.0
+ Revision: 385236
- Update to new version 0.8.0

* Fri May 01 2009 Frederik Himpe <fhimpe@mandriva.org> 0.8.0-0.rc2.1mdv2010.0
+ Revision: 370125
- Update to new version 0.8.0 rc2
- Upstream uses autoconf/automake now, so adapt SPEC file accordingly

* Sat Jan 31 2009 Funda Wang <fwang@mandriva.org> 0.8.0-0.rc1.1mdv2009.1
+ Revision: 335685
- BR makedepend
- 0.8.0 rc1

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.7.3-2mdv2009.0
+ Revision: 267819
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun May 18 2008 Frederik Himpe <fhimpe@mandriva.org> 0.7.3-1mdv2009.0
+ Revision: 208762
- New version, Makefile patch not needed anymore
- Adapt to new license policy
- Package some more interesting %%doc files

  + Thierry Vignaud <tv@mandriva.org>
    - fix spacing at top of description
    - kill extra spacing at top of description

* Mon Jan 28 2008 Funda Wang <fwang@mandriva.org> 0.7.2-1mdv2008.1
+ Revision: 159005
- fix building on x86_64 arch
- rediff Makefile patch

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - new version

* Mon Jul 09 2007 Funda Wang <fwang@mandriva.org> 0.7.1-2mdv2008.0
+ Revision: 50578
- Obsoletes old major
- fix build in x86_64
- New version


* Fri Jul 14 2006 Till Kamppeter <till@mandriva.com> 0.6.5-0.1mdv2007.0
- Updated to version 0.6.5rc2.

* Tue Feb 01 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.6.4-1mdk
- 0.6.4

* Sun Nov 28 2004 Till Kamppeter <till@mandrakesoft.com> 0.6.3-1mdk
- Updated to version 0.6.3.
- New URL.

* Mon Nov 01 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.5-3mdk
- add BuildRequires: libieee1284-devel

