# ansible-role-nginx [![Build Status](https://travis-ci.org/izumimatsuo/ansible-role-nginx.svg?branch=master)](https://travis-ci.org/izumimatsuo/ansible-role-nginx)

CentOS 7 に Nginx Web サーバを導入する ansible role です。

以下のセキュリティ設定を反映済み。

- サーバ情報の隠蔽
- ディレクトリリスティングの無効化
- クリックジャッキング対策
- スニッフィング対策
- クロスサイトスクリプティング対策

## 設定項目

以下の設定項目は上書き可能。

| 項目名            | デフォルト値 | 説明                     |
| ----------------- | ------------ | ------------------------ |
| nginx_listen_port | 80           | ポート番号                |
| nginx_server_name | localhost    | サーバ名                  |
| nginx_ssl_on      | no           | SSL通信を適用する（ポート番号は 443固定） |
| nginx_is_proxy    | no           | reverse proxy として構成 |
| nginx_proxy_backends | localhost:8080 | proxy backend リスト |
| nginx_proxy_dyna_name | app      | 動的構成する際のサービス名 |
| nginx_cluster     | None         | クラスタ情報設定 {virtual_ipaddr: xxx, check_interface: yyy} |

## ログフォーマット

以下の内容を出力。

| 項目名           | 説明                       |
| ---------------- | -------------------------- |
| $remote_addr     | リモートホスト名           |
| "-"              | "-" 表示                   |
| $remote_user     | リモートユーザ             |
| $time_local      | リクエストを受け付けた日時 |
| $request         | リクエストの最初の行       |
| $status          | ステータスコード           |
| $body_bytes_sent | レスポンスのバイト数       |
| $http_referer    | リファラー                 |
| $http_user_agent | エージェント               |
| $request_time    | レスポンス時間、ミリ秒まで |
