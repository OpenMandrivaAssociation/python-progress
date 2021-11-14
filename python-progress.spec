# Created by pyp2rpm-0.5.2
%global pypi_name progress

Name:           python-%{pypi_name}
Version:	1.6
Release:	1
Summary:        Easy to use progress bars
Group:          Development/Python
License:        ISC
URL:            http://github.com/verigak/progress/
Source0:	https://files.pythonhosted.org/packages/2a/68/d8412d1e0d70edf9791cbac5426dc859f4649afc22f2abbeb0d947cf70fd/progress-1.6.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description
Collection of easy to use progress bars and spinners.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
