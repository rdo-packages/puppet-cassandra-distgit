%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name cassandra
%global commit 0fc5e6541e888289c1ea56dc6256f23a729ee68e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-cassandra
Version:        2.1.1
Release:        1%{?alphatag}%{?dist}'
Summary:        Installs Cassandra, DataStax Agent & OpsCenter on RHEL/Ubuntu/Debian.
License:        Apache-2.0

URL:            http://locp.github.io/cassandra

Source0:        https://github.com/locp/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

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
* Tue Nov 15 2016 Alfredo Moralejo <amoralej@redhat.com> 2.1.1-1.0fc5e65.git
- Newton update 2.1.1 (0fc5e6541e888289c1ea56dc6256f23a729ee68e)

* Tue Nov 01 2016 Jon Schlueter <jschluet@redhat.com> 2.1.0-1
- Update to 2.1.0 (80e0f37ee2f2cb801620e5f4ffe089d21a35b573)

* Thu Oct 27 2016 Jon Schlueter <jschluet@redhat.com> 2.0.2-1
- Update to 2.0.2 (6ef74313278a57d2d05b1b32f29750c7979ab01b)

* Thu Sep 22 2016 Haikel Guemar <hguemar@fedoraproject.org> - 1.25.2-1
- Newton update 1.25.2 (698dc80d501fc7b2cedf3d88d1c9fdb6630a2d8f)


