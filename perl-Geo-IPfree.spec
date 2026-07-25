%define upstream_name 	 Geo-IPfree
%define upstream_version 1.160001

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Look up country by IP Address
License:	GPL+ or Artistic
Url:		https://github.com/bricas/geo-ipfree
Group:		Development/Perl
Source0:	https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/Geo-IPfree-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Look up country of IP Address. This module make this off-line and 
the DB of IPs is free & small. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Geo
%{_mandir}/*/*
