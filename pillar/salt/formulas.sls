# -*- coding: utf-8 -*-
# vim: set syntax=yaml ts=2 sw=2 sts=2 et :

# WARNING:  git formulas may not be secure since they are not verified.
# true enables, false disables
enable_gitfs: false

salt_formulas:
  git_opts:
    # The Git options can be customized differently for each
    # environment, if an option is missing in a given environment, the
    # value from "default" is used instead.
    user:
      # URL where the formulas git repositories are downloaded from
      # it will be suffixed with <formula-name>.git
      baseurl: https://github.com/saltstack-formulas
      # Directory where Git repositories are downloaded
      basedir: /srv/user_formulas/user
      # Update the git repository to the latest version (False by default)
      update: False
      # Options passed directly to the git.latest state
      options:
        rev: master

  # Options of the file.directory state that creates the directory where
  # the git repositories of the formulas are stored
  basedir_opts:
    makedirs: True
    user: root
    group: root
    mode: 750

  # List of formulas to enable in each environment
  list:
    user:
      # Formulas to set up http://docs.saltstack.com
      - salt-docs-formula

      # This formula ensures that a sysctl parameter is present on the system
      # from a pillar file.
      - sysctl-formula

      # A formula to install and configure rsync as daemon process.
      - rsyncd-formula

      # This formula installs and configures system locales.
      - locale-formula

      # Formula to configure timezone.
      - timezone-formula

      # Mopidy plays music from local disk, Spotify, SoundCloud, Google Play
      # Music, and more.
      - mopidy-formula

      # Sensu: A monitoring framework that aims to be simple, malleable, and
      # scalable.
      - sensu-formula

      # This module manages your firewall using iptables with pillar configured
      # rules. Thanks to the nature of Pillars it is possible to write global
      # and local settings (e.g. enable globally, configure locally)
      - iptables-formula

      # A networking formula for debian style distributions
      {% if grains['os_family']|lower == 'debian' %}
      - network-debian-formula
      {% endif %}

      # os-hardening formula currently supported for Ubuntu.
      {% if grains['os']|lower == 'ubuntu' %}
      - os-hardening-formula
      {% endif %}

      # Flexible provisioning for JDK and JRE tarballs
      - sun-java-formula

      # Mumble is an open source, low-latency, high quality voice chat software
      # primarily intended for use while gaming.
      - mumble-server-formula

      # Use pillar and scheduler to backup something, anything to the cloud.
      - backuptocloud-formula

      # Tinyproxy is a HTTP proxy server daemon for POSIX operating systems.
      # Designed to be fast and small, it is useful when an HTTP/HTTPS proxy is
      # required, but the system resources for a larger proxy are unavailable.
      - tinyproxy-formula

      # Samba is a free software re-implementation of the SMB/CIFS networking
      # protocol.
      - samba-formula

      # Required for various Debian packages
      {% if grains['os_family']|lower == 'debian' %}
      - build-essential-formula
      {% endif %}

      # Installs screen, as well as a default .screenrc to
      # /usr/local/etc/.screenrc. The .screenrc included is just an example.
      - screen-formula
