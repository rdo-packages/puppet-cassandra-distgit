%global milestone .0rc0
%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-cassandra
%global commit 89bf2d1d2393bb85677d95631089b2e57f15fee2
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-cassandra
Version:        3.1.1
Release:        0.4%{?milestone}%{?alphatag}%{?dist}
Summary:        Installs Cassandra, DataStax Agent & OpsCenter on RHEL/Ubuntu/Debian.
License:        ASL 2.0

URL:            https://github.com/voxpupuli/puppet-cassandra

Source0:        https://github.com/voxpupuli/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

#Requires:       puppet-apt
Requires:       puppet-firewall
Requires:       puppet-inifile
Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Installs Cassandra, DataStax Agent & OpsCenter on RHEL/Ubuntu/Debian.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/cassandra/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/cassandra/



%files
%{_datadir}/openstack-puppet/modules/cassandra/


%changelog
* Fri Apr 01 2022 RDO <dev@lists.rdoproject.org> 3.1.1-0.4.0rc0.89bf2d1git
- Update to post 3.1.1-rc0 (89bf2d1d2393bb85677d95631089b2e57f15fee2)



