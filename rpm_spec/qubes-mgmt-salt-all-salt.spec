%{!?version: %define version %(cat version)}

Name:      qubes-mgmt-salt-all-salt
Version:   %{version}
Release:   1%{?dist}
Summary:   Salt formula to configure salt itself
License:   GPL 2.0
URL:	   http://www.qubes-os.org/

Group:     System administration tools
BuildArch: noarch
Requires:  qubes-mgmt-salt
Requires:  ca-certificates
Requires:  git
Requires:  python-dulwich

%define _builddir %(pwd)

%description
Salt formula to configure salt itself.

%prep
# we operate on the current directory, so no need to unpack anything
# symlink is to generate useful debuginfo packages
rm -f %{name}-%{version}
ln -sf . %{name}-%{version}
%setup -T -D

%build

%install
make install DESTDIR=%{buildroot} LIBDIR=%{_libdir} BINDIR=%{_bindir} SBINDIR=%{_sbindir} SYSCONFDIR=%{_sysconfdir}

%post
# Update Salt Configuration
qubesctl state.sls config -l quiet --out quiet > /dev/null || true
qubesctl saltutil.clear_cache -l quiet --out quiet > /dev/null || true
qubesctl saltutil.sync_all refresh=true -l quiet --out quiet > /dev/null || true

# Enable States
qubesctl top.enable salt.formulas saltenv=all -l quiet --out quiet > /dev/null || true
qubesctl top.enable salt.gitfs.dulwich saltenv=all -l quiet --out quiet > /dev/null || true

# Enable Pillar States
qubesctl top.enable salt.formulas saltenv=all pillar=true -l quiet --out quiet > /dev/null || true

%files
%defattr(-,root,root)
%doc LICENSE README.rst
%attr(750, root, root) %dir /srv/formulas/all/salt-formula
/srv/formulas/all/salt-formula/LICENSE
/srv/formulas/all/salt-formula/pillar.example
/srv/formulas/all/salt-formula/README.rst
/srv/formulas/all/salt-formula/salt/api.sls
/srv/formulas/all/salt-formula/salt/cloud.sls
/srv/formulas/all/salt-formula/salt/defaults.yaml
/srv/formulas/all/salt-formula/salt/files/cloud.maps.d/ec2.conf
/srv/formulas/all/salt-formula/salt/files/cloud.maps.d/gce.conf
/srv/formulas/all/salt-formula/salt/files/cloud.maps.d/rsos.conf
/srv/formulas/all/salt-formula/salt/files/cloud.maps.d/saltify.conf
/srv/formulas/all/salt-formula/salt/files/cloud.profiles.d/ec2.conf
/srv/formulas/all/salt-formula/salt/files/cloud.profiles.d/gce.conf
/srv/formulas/all/salt-formula/salt/files/cloud.profiles.d/rsos.conf
/srv/formulas/all/salt-formula/salt/files/cloud.profiles.d/saltify.conf
/srv/formulas/all/salt-formula/salt/files/cloud.providers.d/ec2.conf
/srv/formulas/all/salt-formula/salt/files/cloud.providers.d/gce.conf
/srv/formulas/all/salt-formula/salt/files/cloud.providers.d/rsos.conf
/srv/formulas/all/salt-formula/salt/files/cloud.providers.d/saltify.conf
/srv/formulas/all/salt-formula/salt/files/key
/srv/formulas/all/salt-formula/salt/files/master.d/f_defaults.conf
/srv/formulas/all/salt-formula/salt/files/master.d/reactor.conf
/srv/formulas/all/salt-formula/salt/files/minion.d/f_defaults.conf
/srv/formulas/all/salt-formula/salt/files/roster.jinja
/srv/formulas/all/salt-formula/salt/formulas.jinja
/srv/formulas/all/salt-formula/salt/formulas.sls
/srv/formulas/all/salt-formula/salt/formulas.top
/srv/formulas/all/salt-formula/salt/gitfs/dulwich.sls
/srv/formulas/all/salt-formula/salt/gitfs/dulwich.top
/srv/formulas/all/salt-formula/salt/gitfs/gitpython.sls
/srv/formulas/all/salt-formula/salt/gitfs/pygit2.sls
/srv/formulas/all/salt-formula/salt/map.jinja
/srv/formulas/all/salt-formula/salt/master.sls
/srv/formulas/all/salt-formula/salt/minion.sls
/srv/formulas/all/salt-formula/salt/pkgrepo/absent.sls
/srv/formulas/all/salt-formula/salt/pkgrepo/debian/absent.sls
/srv/formulas/all/salt-formula/salt/pkgrepo/debian/init.sls
/srv/formulas/all/salt-formula/salt/pkgrepo/debian/saltstack.gpg
/srv/formulas/all/salt-formula/salt/pkgrepo/debian/sources.list
/srv/formulas/all/salt-formula/salt/pkgrepo/init.sls
/srv/formulas/all/salt-formula/salt/pkgrepo/pkgrepo.top
/srv/formulas/all/salt-formula/salt/pkgrepo/redhat/absent.sls
/srv/formulas/all/salt-formula/salt/pkgrepo/redhat/init.sls
/srv/formulas/all/salt-formula/salt/pkgrepo/ubuntu/absent.sls
/srv/formulas/all/salt-formula/salt/pkgrepo/ubuntu/init.sls
/srv/formulas/all/salt-formula/salt/ssh.sls
/srv/formulas/all/salt-formula/salt/standalone.sls
/srv/formulas/all/salt-formula/salt/syndic.sls

%attr(750, root, root) %dir /srv/pillar/all/salt
%config(noreplace) /srv/pillar/all/salt/formulas.sls
/srv/pillar/all/salt/formulas.top

%changelog
