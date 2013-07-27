%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global with_python3 1
%global upstream_name redis

Name:           python-%{upstream_name}
Version:        2.7.6
Release:        1%{?dist}
Summary:        A Python client for redis

Group:          Development/Languages
License:        MIT
URL:            http://github.com/andymccurdy/redis-py
Source0:        http://pypi.python.org/packages/source/r/redis/redis-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-py

%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-py
%endif

%description
This is a Python interface to the Redis key-value store.

%if 0%{?with_python3}
%package -n python3-redis
Summary:        A Python3 client for redis
Group:          Development/Languages

%description -n python3-redis
This is a Python interface to the Redis key-value store.
%endif

%prep
%setup -q -n %{upstream_name}-%{version}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%{__python} setup.py build

%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root=%{buildroot}
popd
%endif

%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%check
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py test
popd
%endif

%{__python} setup.py test

%files
%defattr(-,root,root,-)
%doc CHANGES LICENSE README.rst
%{python_sitelib}/%{upstream_name}
%{python_sitelib}/%{upstream_name}-%{version}-*.egg-info

%if 0%{?with_python3}
%files -n python3-redis
%defattr(-,root,root,-)
%doc CHANGES LICENSE README.rst
%{python3_sitelib}/%{upstream_name}
%{python3_sitelib}/%{upstream_name}-%{version}-*.egg-info
%endif

%changelog
* Sat Jul 27 2013 Luke Macken <lmacken@redhat.com> - 2.7.6-1
- Update to 2.7.6
- Run the test suite
- Add a python3 subpackage
- Remove obsolete buildroot tag and cleanup

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 27 2012 Silas Sewell <silas@sewell.org> - 2.7.2-1
- Update to 2.7.2

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jul 24 2011 Silas Sewell <silas@sewell.org> - 2.4.9-1
- Update to 2.4.9

* Sun Mar 27 2011 Silas Sewell <silas@sewell.ch> - 2.2.4-1
- Update to 2.2.4

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Sep 04 2010 Silas Sewell <silas@sewell.ch> - 2.0.0-1
- Initial build
