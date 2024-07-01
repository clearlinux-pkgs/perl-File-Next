#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-Next
Version  : 1.18
Release  : 28
URL      : https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/File-Next-1.18.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/File-Next-1.18.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-next-perl/libfile-next-perl_1.16-2.debian.tar.xz
Summary  : 'File-finding iterator'
Group    : Development/Tools
License  : Artistic-2.0 GPL-2.0 MIT
Requires: perl-File-Next-license = %{version}-%{release}
Requires: perl-File-Next-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
File-Next
---------
[![Build Status](https://travis-ci.org/petdance/file-next.svg?branch=dev)](https://travis-ci.org/petdance/file-next)

%package dev
Summary: dev components for the perl-File-Next package.
Group: Development
Provides: perl-File-Next-devel = %{version}-%{release}
Requires: perl-File-Next = %{version}-%{release}

%description dev
dev components for the perl-File-Next package.


%package license
Summary: license components for the perl-File-Next package.
Group: Default

%description license
license components for the perl-File-Next package.


%package perl
Summary: perl components for the perl-File-Next package.
Group: Default
Requires: perl-File-Next = %{version}-%{release}

%description perl
perl components for the perl-File-Next package.


%prep
%setup -q -n File-Next-1.18
cd %{_builddir}
tar xf %{_sourcedir}/libfile-next-perl_1.16-2.debian.tar.xz
cd %{_builddir}/File-Next-1.18
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/File-Next-1.18/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-Next
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-File-Next/a72be0e36cf1bb7d61766c95b639de45698e278b
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::Next.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-Next/a72be0e36cf1bb7d61766c95b639de45698e278b

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
