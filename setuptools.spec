#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : setuptools
Version  : 40.6.2
Release  : 134
URL      : https://files.pythonhosted.org/packages/b0/d1/8acb42f391cba52e35b131e442e80deffbb8d0676b93261d761b1f0ef8fb/setuptools-40.6.2.zip
Source0  : https://files.pythonhosted.org/packages/b0/d1/8acb42f391cba52e35b131e442e80deffbb8d0676b93261d761b1f0ef8fb/setuptools-40.6.2.zip
Summary  : Easily download, build, install, upgrade, and uninstall Python packages
Group    : Development/Tools
License  : MIT Python-2.0 ZPL-2.0
Requires: setuptools-bin = %{version}-%{release}
Requires: setuptools-license = %{version}-%{release}
Requires: setuptools-python = %{version}-%{release}
Requires: setuptools-python3 = %{version}-%{release}
Requires: certifi
Requires: setuptools
BuildRequires : buildreq-distutils3
BuildRequires : setuptools

%description
.. image:: https://img.shields.io/pypi/v/setuptools.svg
:target: https://pypi.org/project/setuptools

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

%description python3
python3 components for the setuptools package.


%prep
%setup -q -n setuptools-40.6.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542110311
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/setuptools
cp LICENSE %{buildroot}/usr/share/package-licenses/setuptools/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
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
%defattr(0644,root,root,0755)
/usr/share/package-licenses/setuptools/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
