%define module 	Geo-IPfree
%define version 0.2
%define release %mkrel 4

Summary:	Look up country by IP Address
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
Url:		http://search.cpan.org/dist/%{module}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
Buildarch:	noarch

%description
Look up country of IP Address. This module make this off-line and 
the DB of IPs is free & small. 

%prep
%setup -q -n %{module}-%{version}

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

