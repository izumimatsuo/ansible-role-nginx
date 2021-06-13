# ansible-role-nginx [![Build Status](https://travis-ci.org/izumimatsuo/ansible-role-nginx.svg?branch=master)](https://travis-ci.org/izumimatsuo/ansible-role-nginx)

CentOS 7 に Nginx Web サーバを導入する ansible role です。

- nginx_proxy_backends を設定する事で reverse proxy として動作させられる
- nginx_cluster_info を設定する事で 1+1 (Active/Standby) クラスタを構成できる

以下のセキュリティ設定を反映済み。

- サーバ情報の隠蔽
- ディレクトリリスティングの無効化
- クリックジャッキング対策
- スニッフィング対策
- クロスサイトスクリプティング対策

SSL 通信するために、以下のとおりに証明書等が配置されていること

- /etc/nginx/cert/server.crt
- /etc/nginx/cert/server.key

## 設定項目

以下の設定項目は上書き可能。

| 項目名            | デフォルト値 | 説明                     |
| ----------------- | ------------ | ------------------------ |
| nginx_ssl_on      | yes          | SSL通信を適用する          |
| nginx_listen_port | 443          | ポート番号（SSL通信適用を設定しない場合は 80 に自動変更） |
| nginx_server_name | localhost    | サーバ名                  |
| nginx_proxy_backends | None      | proxy backend リスト |

