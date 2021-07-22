#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipaddr
Version  : 2.2.0
Release  : 49
URL      : http://pypi.debian.net/ipaddr/ipaddr-2.2.0.tar.gz
Source0  : http://pypi.debian.net/ipaddr/ipaddr-2.2.0.tar.gz
Summary  : Google's IP address manipulation library
Group    : Development/Tools
License  : Apache-2.0
Requires: ipaddr-license = %{version}-%{release}
Requires: ipaddr-python = %{version}-%{release}
Requires: ipaddr-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
It has been superseded by ipaddress from the Python 3 standard library, and its
        Python 2 backport.

%package license
Summary: license components for the ipaddr package.
Group: Default

%description license
license components for the ipaddr package.


%package python
Summary: python components for the ipaddr package.
Group: Default
Requires: ipaddr-python3 = %{version}-%{release}

%description python
python components for the ipaddr package.


%package python3
Summary: python3 components for the ipaddr package.
Group: Default
Requires: python3-core
Provides: pypi(ipaddr)

%description python3
python3 components for the ipaddr package.


%prep
%setup -q -n ipaddr-2.2.0
cd %{_builddir}/ipaddr-2.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603393351
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python ipaddr_test.py
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ipaddr
cp %{_builddir}/ipaddr-2.2.0/COPYING %{buildroot}/usr/share/package-licenses/ipaddr/b12b78a934ce210fd844569263f587c14a8a14fd
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ipaddr/b12b78a934ce210fd844569263f587c14a8a14fd

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
