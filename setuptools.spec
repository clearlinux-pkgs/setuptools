#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : setuptools
Version  : 35.0.2
Release  : 66
URL      : https://pypi.debian.net/setuptools/setuptools-35.0.2.zip
Source0  : https://pypi.debian.net/setuptools/setuptools-35.0.2.zip
Summary  : Easily download, build, install, upgrade, and uninstall Python packages
Group    : Development/Tools
License  : MIT Python-2.0 ZPL-2.0
Requires: setuptools-bin
Requires: setuptools-python
Requires: Sphinx
Requires: appdirs
Requires: certifi
Requires: packaging
Requires: setuptools
Requires: six
BuildRequires : appdirs
BuildRequires : packaging
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : testrepository
BuildRequires : testresources
BuildRequires : testscenarios
BuildRequires : testtools

%description
.. image:: https://readthedocs.org/projects/setuptools/badge/?version=latest
:target: https://setuptools.readthedocs.io

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
%setup -q -n setuptools-35.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1493410742
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 || :
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
/usr/lib/python2*/*
