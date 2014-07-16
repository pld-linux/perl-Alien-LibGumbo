# TODO:
# - make it use gumbo-parser-devel
#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Alien
%define		pnam	LibGumbo
%include	/usr/lib/rpm/macros.perl
Summary:	gumbo parser library
Name:		perl-Alien-LibGumbo
Version:	0.02
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Alien/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9dbcfb65d56c17c09082079bbb42848c
URL:		http://search.cpan.org/dist/Alien-LibGumbo/
BuildRequires:	gumbo-parser-devel
BuildRequires:	perl-Alien-Base
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gumbo parser library.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

DESTDIR=$RPM_BUILD_ROOT \
	./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Alien/*.pm
%{perl_vendorlib}/Alien/LibGumbo
%{_mandir}/man3/*
