{% from "salt/map.jinja" import salt_settings with context %}

salt-standalone-config:
  file.recurse:
    - name: {{ salt_settings.config_path }}/minion.d
    - template: jinja
    - source: salt://{{ slspath }}/files/minion.d
    - clean: {{ salt_settings.clean_config_d_dir }}
    - exclude_pat: _*
    - context:
        standalone: True
  service.dead:
    - enable: False
    - name: {{ salt_settings.minion_service }}
    - require:
      - file: salt-standalone-config
