# TODO:
# - make it use gumbo-parser-devel
# - https://github.com/ruz/Alien-LibGumbo/issues/2
#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Alien
%define		pnam	LibGumbo
Summary:	Alien::LibGumbo - Gumbo parser library
Summary(pl.UTF-8):	Alien::LibGumbo - biblioteka analizatora Gumbo
Name:		perl-Alien-LibGumbo
Version:	0.05
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Alien/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	afeadf69135fbf368695e3d780c414da
URL:		https://metacpan.org/release/Alien-LibGumbo
BuildRequires:	gumbo-parser-devel
BuildRequires:	perl-Alien-Base >= 0.005
BuildRequires:	perl-File-ShareDir >= 1.03
BuildRequires:	perl-Module-Build >= 0.42
BuildRequires:	perl-Path-Class >= 0.013
BuildRequires:	perl-devel >= 1:5.10.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
Requires:	gumbo-parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package brings libgumbo: <https://github.com/google/gumbo-parser>
on your system for use by Perl modules like HTML::Gumbo.

%description -l pl.UTF-8
Ten pakiet udostępnia w systemie libgumbo
(<https://github.com/google/gumbo-parser>) dla modułów Perla, takich
jak HTML::Gumbo.

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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/auto/share/dist/Alien-LibGumbo/README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Alien/LibGumbo.pm
%{perl_vendorlib}/Alien/LibGumbo
%{_mandir}/man3/Alien::LibGumbo.3pm*
%{_mandir}/man3/Alien::LibGumbo::ConfigData.3pm*
