# ansible-role-nginx

Nginx Web サーバを構築する ansible role です。

以下のセキュリティ設定を反映。

* バージョン情報の隠蔽
* ディレクトリリスティングの無効化
* クリックジャッキング対策


## ビルド

ansible-playbook と testinfra の実行コンテナをビルド＆テスト実行

ビルド実行

``` $ ./build.sh ```
