# -*- coding:utf8 -*-

def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed
    assert nginx.version.startswith("1.14")

def test_nginx_running_and_enabled(host):
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled

def test_nginx_is_listen(host):
    assert host.socket("tcp://0.0.0.0:80").is_listening
