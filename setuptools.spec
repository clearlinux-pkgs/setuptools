#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : setuptools
Version  : 24.0.1
Release  : 53
URL      : http://pypi.debian.net/setuptools/setuptools-24.0.1.tar.gz
Source0  : http://pypi.debian.net/setuptools/setuptools-24.0.1.tar.gz
Summary  : Easily download, build, install, upgrade, and uninstall Python packages
Group    : Development/Tools
License  : Python-2.0 ZPL-2.0
Requires: setuptools-bin
Requires: setuptools-python
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
===============================
Installing and Using Setuptools
===============================

%package bin
Summary: bin components for the setuptools package.
Group: Binaries

%description bin
bin components for the setuptools package.


%package python
Summary: python components for the setuptools package.
Group: Default

%description python
python components for the setuptools package.


%prep
%setup -q -n setuptools-24.0.1

%build
export LANG=C
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/easy_install
/usr/bin/easy_install-2.7

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
