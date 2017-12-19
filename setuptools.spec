#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : setuptools
Version  : 38.2.4
Release  : 98
URL      : https://pypi.debian.net/setuptools/setuptools-38.2.4.zip
Source0  : https://pypi.debian.net/setuptools/setuptools-38.2.4.zip
Summary  : Easily download, build, install, upgrade, and uninstall Python packages
Group    : Development/Tools
License  : MIT Python-2.0 ZPL-2.0
Requires: setuptools-bin
Requires: setuptools-legacypython
Requires: setuptools-python3
Requires: setuptools-python
Requires: certifi
Requires: setuptools
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : testrepository
BuildRequires : testresources
BuildRequires : testscenarios
BuildRequires : testtools

%description
.. image:: https://img.shields.io/pypi/v/setuptools.svg
:target: https://pypi.org/project/setuptools

%package bin
Summary: bin components for the setuptools package.
Group: Binaries

%description bin
bin components for the setuptools package.


%package extras
Summary: extras components for the setuptools package.
Group: Default

%description extras
extras components for the setuptools package.


%package legacypython
Summary: legacypython components for the setuptools package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the setuptools package.


%package python
Summary: python components for the setuptools package.
Group: Default
Requires: setuptools-legacypython
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
%setup -q -n setuptools-38.2.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1512436252
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 || :
%install
export SOURCE_DATE_EPOCH=1512436252
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/easy_install-2.7
/usr/bin/easy_install
/usr/bin/easy_install-3.6

%files extras
%defattr(-,root,root,-)
/usr/bin/easy_install-2.7

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
