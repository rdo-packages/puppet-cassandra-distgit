%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-cassandra
%global commit a371404eb9342a6c3973b0414a98167049c3f43c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-cassandra
Version:        2.7.4
Release:        0.1%{?alphatag}%{?dist}
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
* Thu Feb 15 2018 RDO <dev@lists.rdoproject.org> 2.7.4-0.1.a371404git
- Update to pre-release 2.7.4 (a371404eb9342a6c3973b0414a98167049c3f43c)



