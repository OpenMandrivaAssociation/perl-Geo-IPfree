%define upstream_name 	 Geo-IPfree
%define upstream_version 1.111650

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Look up country by IP Address
License:	GPL+ or Artistic
Url:		http://search.cpan.org/dist/%{upstream_name}
Group:		Development/Perl
Source0:	http://www.cpan.org/modules/by-module/Geo/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Look up country of IP Address. This module make this off-line and 
the DB of IPs is free & small. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Geo
%{_mandir}/*/*


%changelog
* Wed Jun 15 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.111.650-1mdv2011.0
+ Revision: 685313
- update to new version 1.111650

* Fri Feb 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.110.450-1
+ Revision: 638478
- update to new version 1.110450

* Sat Oct 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.102.870-1mdv2011.0
+ Revision: 587628
- new version

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.101.650-1mdv2011.0
+ Revision: 552311
- update to 1.101650

* Tue Feb 16 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.470-1mdv2010.1
+ Revision: 506747
- update to 1.100470

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.800.0-1mdv2010.1
+ Revision: 461283
- update to 0.8

* Tue Sep 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.700.0-1mdv2010.0
+ Revision: 442939
- update to 0.7

* Sun May 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.6-1mdv2010.0
+ Revision: 376722
- update to new version 0.6

* Wed Feb 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.5-1mdv2009.1
+ Revision: 337313
- update to new version 0.5

* Tue Dec 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.4-1mdv2009.1
+ Revision: 309304
- update to new version 0.4

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.3-1mdv2009.1
+ Revision: 305713
- update to new version 0.3

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.2-6mdv2009.0
+ Revision: 241288
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 0.2-4mdv2008.0
+ Revision: 67506
- simplify buildrequires


* Tue Sep 27 2005 Olivier Thauvin <nanardon@mandriva.org> 0.2-4mdk
- remove MANIFEST

* Tue Sep 27 2005 Olivier Thauvin <nanardon@mandriva.org> 0.2-3mdk
- rebuild
- make test

* Tue Nov 09 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.2-2mdk
- rebuild

* Mon Sep 22 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.2-1mdk
- needed by w3perl

