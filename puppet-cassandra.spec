%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%define upstream_name cassandra

Name:                   puppet-cassandra
Version:                1.26.1
Release:                2%{?dist}
Summary:                Installs Cassandra, DataStax Agent & OpsCenter on RHEL/Ubuntu/Debian
License:                Apache-2.0

URL:                    https://github.com/locp/cassandra

Source0:                https://github.com/locp/cassandra/archive/%{version}.tar.gz

BuildArch:              noarch

Requires:               puppet-firewall
Requires:               puppet-inifile
Requires:               puppet-stdlib

Requires:               puppet >= 2.7.0

%description
Installs Cassandra, DataStax Agent & OpsCenter on RHEL/Ubuntu/Debian

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
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/cassandra/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/cassandra/



%files
%{_datadir}/openstack-puppet/modules/cassandra/


%changelog
