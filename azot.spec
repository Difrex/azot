Name:           azot
Version:        0.1.3
Release:        1%{?dist}
Summary:        Screen corners actions in all WM
License:        BSD
Group:          Python
URL:            https://github.com/Difrex/azot
Source0:        https://github.com/Difrex/azot/archive/%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       python-xlib

%description
Screen corners actions in all WM

%prep
%autosetup

%build

%install
rm -rf $RPM_BUILD_ROOT
rm -f *.pyc
rm -f Azot/*.pyc

mkdir -p $RPM_BUILD_ROOT/usr/lib/python3.4/site-packages/Azot/
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/azot/
mkdir -p $RPM_BUILD_ROOT/usr/bin/

cp README.md $RPM_BUILD_ROOT/usr/share/doc/azot
cp LICENSE $RPM_BUILD_ROOT/usr/share/doc/azot
cp config.sample.json $RPM_BUILD_ROOT/usr/share/doc/azot
cp azot.py $RPM_BUILD_ROOT/usr/bin/
cp azot/* $RPM_BUILD_ROOT/usr/lib/python3.4/site-packages/Azot/

%{_fixperms} $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/azot.py
/usr/lib/python3.4/site-packages/Azot/X.py
/usr/lib/python3.4/site-packages/Azot/X.pyc
/usr/lib/python3.4/site-packages/Azot/X.pyo
/usr/lib/python3.4/site-packages/Azot/__init__.py
/usr/lib/python3.4/site-packages/Azot/__init__.pyc
/usr/lib/python3.4/site-packages/Azot/__init__.pyo
/usr/lib/python3.4/site-packages/Azot/action.py
/usr/lib/python3.4/site-packages/Azot/action.pyc
/usr/lib/python3.4/site-packages/Azot/action.pyo
/usr/lib/python3.4/site-packages/Azot/config.py
/usr/lib/python3.4/site-packages/Azot/config.pyc
/usr/lib/python3.4/site-packages/Azot/config.pyo
/usr/lib/python3.4/site-packages/Azot/logger.py
/usr/lib/python3.4/site-packages/Azot/logger.pyc
/usr/lib/python3.4/site-packages/Azot/logger.pyo
%defattr(-,root,root,-)
%doc  LICENSE README.md config.sample.json

%changelog
* Tue Jul 28 2015 Difrex 0.1.3
- Warnings
- Fix crashes
* Wed Jul 22 2015 Difrex 0.1.2
- Add specfile
