#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : setuptools
Version  : 56.2.0
Release  : 206
URL      : https://files.pythonhosted.org/packages/fc/0a/b486efab52f8ad03c3eca0c998dd3deafba0c39b29e0c49c68a7152c8b2d/setuptools-56.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/fc/0a/b486efab52f8ad03c3eca0c998dd3deafba0c39b29e0c49c68a7152c8b2d/setuptools-56.2.0.tar.gz
Summary  : Easily download, build, install, upgrade, and uninstall Python packages
Group    : Development/Tools
License  : MIT Python-2.0 ZPL-2.0
Requires: setuptools-bin = %{version}-%{release}
Requires: setuptools-license = %{version}-%{release}
Requires: setuptools-python = %{version}-%{release}
Requires: setuptools-python3 = %{version}-%{release}
Requires: certifi
BuildRequires : buildreq-distutils3
BuildRequires : certifi
BuildRequires : setuptools

%description
.. image:: https://img.shields.io/pypi/v/setuptools.svg
:target: `PyPI link`_
.. image:: https://img.shields.io/pypi/pyversions/setuptools.svg
:target: `PyPI link`_

%package bin
Summary: bin components for the setuptools package.
Group: Binaries
Requires: setuptools-license = %{version}-%{release}

%description bin
bin components for the setuptools package.


%package license
Summary: license components for the setuptools package.
Group: Default

%description license
license components for the setuptools package.


%package python
Summary: python components for the setuptools package.
Group: Default
Requires: setuptools-python3 = %{version}-%{release}

%description python
python components for the setuptools package.


%package python3
Summary: python3 components for the setuptools package.
Group: Default
Requires: python3-core
Provides: pypi(setuptools)

%description python3
python3 components for the setuptools package.


%prep
%setup -q -n setuptools-56.2.0
cd %{_builddir}/setuptools-56.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1620752427
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/setuptools
cp %{_builddir}/setuptools-56.2.0/LICENSE %{buildroot}/usr/share/package-licenses/setuptools/8e6689d37f82d5617b7f7f7232c94024d41066d1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
mkdir -p %{buildroot}/usr/bin
echo "#!/bin/sh" > %{buildroot}/usr/bin/easy_install_is_deprecated
chmod 755 %{buildroot}/usr/bin/easy_install_is_deprecated
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/easy_install_is_deprecated

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/setuptools/8e6689d37f82d5617b7f7f7232c94024d41066d1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
