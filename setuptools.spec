#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : setuptools
Version  : 59.1.1
Release  : 228
URL      : https://files.pythonhosted.org/packages/33/68/e72f8c047e7f25b20c9df02163d925dc734bbee46597018e122a2bce9d3e/setuptools-59.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/33/68/e72f8c047e7f25b20c9df02163d925dc734bbee46597018e122a2bce9d3e/setuptools-59.1.1.tar.gz
Summary  : Easily download, build, install, upgrade, and uninstall Python packages
Group    : Development/Tools
License  : MIT Python-2.0 ZPL-2.0
Requires: setuptools-bin = %{version}-%{release}
Requires: setuptools-license = %{version}-%{release}
Requires: setuptools-python = %{version}-%{release}
Requires: setuptools-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : setuptools

%description
.. image:: https://raw.githubusercontent.com/pypa/setuptools/main/docs/images/banner-640x320.svg
:align: center

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
%setup -q -n setuptools-59.1.1
cd %{_builddir}/setuptools-59.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1637079422
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/setuptools
cp %{_builddir}/setuptools-59.1.1/LICENSE %{buildroot}/usr/share/package-licenses/setuptools/8e6689d37f82d5617b7f7f7232c94024d41066d1
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
