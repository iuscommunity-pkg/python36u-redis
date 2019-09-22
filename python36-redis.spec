%global upstream_name redis
%global python python36

%if %{defined el6}
%global __python3 /usr/bin/python3.6
%endif

%bcond_with tests

Name:           %{python}-%{upstream_name}
Version:        2.10.6
Release:        2%{?dist}
Summary:        Python interface to the Redis key-value store
License:        MIT
URL:            https://github.com/andymccurdy/redis-py
Source0:        https://pypi.io/packages/source/r/redis/%{upstream_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{python}-devel
BuildRequires:  %{python}-setuptools
%if %{with tests}
BuildRequires:  %{python}-py
BuildRequires:  %{python}-pytest
BuildRequires:  redis
%endif

# Rename from python36u-redis
Provides: python36u-%{srcname} = %{version}-%{release}
Obsoletes: python36u-%{srcname} < 2.10.6-2


%description
This is a Python 3 interface to the Redis key-value store.


%prep
%setup -qn %{upstream_name}-%{version}
rm -frv %{upstream_name}.egg-info

%if %{with tests}
# This test passes locally but fails in koji...
rm tests/test_commands.py*
%endif


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
redis-server &
%{__python3} setup.py test
kill %1
%endif


%files
%license LICENSE
%doc CHANGES README.rst
%{python3_sitelib}/%{upstream_name}
%{python3_sitelib}/%{upstream_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Sat Sep 21 2019 Carl George <carl@george.computer> - 2.10.6-2
- Rename to python36-redis
- Switch to EPEL python3 macros

* Thu Aug 17 2017 Ben Harper <ben.harper@rackspace.com> - 2.10.6-1.ius
- Latest upstream
- update Source0

* Thu Apr 06 2017 Carl George <carl.george@rackspace.com> - 2.10.5-1.ius
- Port from Fedora to IUS
- Properly handle license
- Conditionalize test suite

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.10.5-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.5-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr 04 2016 Ralph Bean <rbean@redhat.com> - 2.10.5-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.3-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Jul 10 2015 Ralph Bean <rbean@redhat.com> - 2.10.3-3
- Remove test that fails erroneously in koji.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Aug 21 2014 Christopher Meng <rpm@cicku.me> - 2.10.3-1
- Update to 2.10.3

* Tue Aug 12 2014 Christopher Meng <rpm@cicku.me> - 2.10.2-1
- Update to 2.10.2

* Thu Jun 19 2014 Christopher Meng <rpm@cicku.me> - 2.10.1-1
- Update to 2.10.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri Feb 14 2014 Christopher Meng <rpm@cicku.me> - 2.9.1-1
- Update to 2.9.1
- Use generated egg instead of bundled egg
- Cleanup again

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
