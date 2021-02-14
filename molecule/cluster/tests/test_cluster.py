import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_keepalived_is_installed(host):
    package = host.package("keepalived")
    assert package.is_installed
    assert package.version.startswith("1.3")


def test_keepalived_running_and_enabled(host):
    keepalived = host.service("keepalived")
    assert keepalived.is_running
    assert keepalived.is_enabled


def test_keepalived_state_and_vip(host):
    state = host.run("journalctl |grep STATE |tail -n 1")
    addresses = host.interface("eth0").addresses

    if 'MASTER' in state.stdout:
        assert '172.17.0.10' in addresses
    else:
        assert '172.17.0.10' not in addresses


def test_nginx_running_and_enabled(host):
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled


def test_nginx_is_listen(host):
    assert host.socket("tcp://0.0.0.0:80").is_listening
