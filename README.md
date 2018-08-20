# ansible-role-nginx

Nginx proxy サーバを構築する ansible role です。

## ビルド

ansible と testinfra の実行コンテナをビルド＆レジスト

``` $ ./start_private_registry.sh ```

ビルド実行

``` $ ./ansible_build.sh ```

ビルド実行（gitlab-runner の場合）

``` $ gitlab-runner exec docker --docker-volumes /var/run/docker.sock:/var/run/docker.sock ansible_build ```
