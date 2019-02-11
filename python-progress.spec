# Created by pyp2rpm-0.5.2
%global pypi_name progress

Name:           python-%{pypi_name}
Version:        1.4
Release:        1
Summary:        Easy to use progress bars
Group:          Development/Python
License:        ISC
URL:            http://github.com/verigak/progress/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools

Patch1:         0001-fixup-moving-average-window.patch


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
