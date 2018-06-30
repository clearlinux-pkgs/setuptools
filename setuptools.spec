#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : setuptools
Version  : 39.2.0
Release  : 122
URL      : https://files.pythonhosted.org/packages/1a/04/d6f1159feaccdfc508517dba1929eb93a2854de729fa68da9d5c6b48fa00/setuptools-39.2.0.zip
Source0  : https://files.pythonhosted.org/packages/1a/04/d6f1159feaccdfc508517dba1929eb93a2854de729fa68da9d5c6b48fa00/setuptools-39.2.0.zip
Summary  : Easily download, build, install, upgrade, and uninstall Python packages
Group    : Development/Tools
License  : MIT Python-2.0 ZPL-2.0
Requires: setuptools-bin
Requires: setuptools-python3
Requires: setuptools-license
Requires: setuptools-python
Requires: certifi
Requires: setuptools
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
.. image:: https://img.shields.io/pypi/v/setuptools.svg
:target: https://pypi.org/project/setuptools

%package bin
Summary: bin components for the setuptools package.
Group: Binaries
Requires: setuptools-license

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
Requires: setuptools-python3

%description python
python components for the setuptools package.


%package python3
Summary: python3 components for the setuptools package.
Group: Default
Requires: python3-core

%description python3
python3 components for the setuptools package.


%prep
%setup -q -n setuptools-39.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530317783
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/setuptools
cp LICENSE %{buildroot}/usr/share/doc/setuptools/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/easy_install
/usr/bin/easy_install-3.7

%files license
%defattr(-,root,root,-)
/usr/share/doc/setuptools/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
