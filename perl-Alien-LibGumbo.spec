# TODO:
# - make it use gumbo-parser-devel
# - https://github.com/ruz/Alien-LibGumbo/issues/2
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
Release:	1
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gumbo parser library.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	create_packlist=0
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Alien/*.pm
%{perl_vendorlib}/Alien/LibGumbo
%dir %{perl_vendorlib}/auto/share/dist/Alien-LibGumbo
%{perl_vendorlib}/auto/share/dist/Alien-LibGumbo/include
%dir %{perl_vendorlib}/auto/share/dist/Alien-LibGumbo/lib
# see TODO
%attr(755,root,root) %{perl_vendorlib}/auto/share/dist/Alien-LibGumbo/lib/libgumbo.so*
%{perl_vendorlib}/auto/share/dist/Alien-LibGumbo/lib/pkgconfig
%{_mandir}/man3/*
