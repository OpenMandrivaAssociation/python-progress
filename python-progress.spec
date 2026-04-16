%define module progress
%bcond tests 1

Name:		python-progress
Version:	1.6.1
Release:	1
Summary:	Easy to use progress bars
Group:		Development/Python
License:	ISC
URL:		https://github.com/verigak/progress/
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(wheel)

%description
Collection of easy to use progress bars and spinners.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%if %{with tests}
%check
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
%{__python} test_progress.py
%endif

%files
%doc README.rst
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
