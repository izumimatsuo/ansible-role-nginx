# ansible-role-nginx

CentOS 7 に Nginx Web サーバを構築する ansible role です。

以下のセキュリティ設定を反映済み。

* サーバ情報の隠蔽
* ディレクトリリスティングの無効化
* クリックジャッキング対策
* クロスサイトスクリプティング対策

## 設定項目

以下の設定項目は上書き可能。

項目名           |デフォルト値|説明
-----------------|------------|----------
nginx_listen_port|80          |ポート番号
nginx_server_name|localhost   |サーバ名

## ログフォーマット

以下の内容を出力。

項目名          |説明
----------------|------------------------------
$remote_addr    |リモートホスト名
　              |"-" 表示
$remote_user    |リモートユーザ
$time_local     |リクエストを受け付けた日時
$request        |リクエストの最初の行
$status         |ステータスコード
$body_bytes_sent|レスポンスのバイト数
$http_referer   |リファラー
$http_user_agent|エージェント
$request_time   |レスポンス時間、ミリ秒まで

## ビルド

以下のいづれかで ansible-playbook と testinfra を実行可能。

1) docker-compose でビルド実行

``` $ ./build.sh ```

2) gitlab-runner でビルド実行

``` $ gitlab-runner exec docker --docker-volumes /var/run/docker.sock:/var/run/docker.sock ansible_build ```
