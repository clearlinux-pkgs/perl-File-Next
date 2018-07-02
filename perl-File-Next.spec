#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-Next
Version  : 1.16
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/File-Next-1.16.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/File-Next-1.16.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-next-perl/libfile-next-perl_1.16-2.debian.tar.xz
Summary  : 'File-finding iterator'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-File-Next-man

%description
File-Next
---------
[![Build Status](https://travis-ci.org/petdance/file-next.svg?branch=dev)](https://travis-ci.org/petdance/file-next)

%package man
Summary: man components for the perl-File-Next package.
Group: Default

%description man
man components for the perl-File-Next package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n File-Next-1.16
mkdir -p %{_topdir}/BUILD/File-Next-1.16/deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/File-Next-1.16/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/File/Next.pm

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/File::Next.3
