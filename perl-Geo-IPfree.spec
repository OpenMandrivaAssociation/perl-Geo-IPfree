%define upstream_name 	 Geo-IPfree
%define upstream_version 0.7

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Look up country by IP Address
License:	GPL+ or Artistic
Url:		http://search.cpan.org/dist/%{upstream_name}
Group:		Development/Perl
Source0:	http://www.cpan.org/modules/by-module/Geo/%{upstream_name}-%{upstream_version}.tar.gz

Buildarch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Geo
%{_mandir}/*/*
