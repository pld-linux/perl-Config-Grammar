#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Config
%define		pnam	Grammar
%include	/usr/lib/rpm/macros.perl
Summary:	Config::Grammar - A grammar-based, user-friendly config parser
Name:		perl-Config-Grammar
Version:	1.10
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Config/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ce904f687f1ee9c70521142a2e0f15c9
URL:		http://search.cpan.org/dist/Config-Grammar/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Config::Grammar is a module to parse configuration files.

The configuration may consist of multiple-level sections with
assignments and tabular data. The parsed data will be returned as a
hash containing the whole configuration. Config::Grammar uses a
grammar that is supplied upon creation of a Config::Grammar object to
parse the configuration file and return helpful error messages in case
of syntax errors. Using the makepod method you can generate
documentation of the configuration file format.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Config/*.pm
%{perl_vendorlib}/Config/Grammar
%{_mandir}/man3/*
