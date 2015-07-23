Name:           azot
Version:        0.1.2
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
rm -f azot/*.pyc

mkdir -p $RPM_BUILD_ROOT/usr/lib/python2.7/site-packages/azot/
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/azot/
mkdir -p $RPM_BUILD_ROOT/usr/bin/

cp README.md $RPM_BUILD_ROOT/usr/share/doc/azot
cp LICENSE $RPM_BUILD_ROOT/usr/share/doc/azot
cp config.sample.json $RPM_BUILD_ROOT/usr/share/doc/azot
cp azot.py $RPM_BUILD_ROOT/usr/bin/
cp azot/* $RPM_BUILD_ROOT/usr/lib/python2.7/site-packages/azot/

%{_fixperms} $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/azot.py
/usr/lib/python2.7/site-packages/azot/X.py
/usr/lib/python2.7/site-packages/azot/X.pyc
/usr/lib/python2.7/site-packages/azot/X.pyo
/usr/lib/python2.7/site-packages/azot/__init__.py
/usr/lib/python2.7/site-packages/azot/__init__.pyc
/usr/lib/python2.7/site-packages/azot/__init__.pyo
/usr/lib/python2.7/site-packages/azot/action.py
/usr/lib/python2.7/site-packages/azot/action.pyc
/usr/lib/python2.7/site-packages/azot/action.pyo
/usr/lib/python2.7/site-packages/azot/config.py
/usr/lib/python2.7/site-packages/azot/config.pyc
/usr/lib/python2.7/site-packages/azot/config.pyo
%defattr(-,root,root,-)
%doc  LICENSE README.md config.sample.json

%changelog
* Wed Jul 22 2015 Difrex 0.1.2
- Add specfile
