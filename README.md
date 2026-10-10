# 魔女と、ハイチーズ。 — わなみフェス AR
公開URL: https://tetosfactory.github.io/wanami-witch-webar/
リポジトリ: https://github.com/tetosfactory/wanami-witch-webar
配布用QR: [QR画像](qr/wanami-witch-qr.png)

## ゴーストARと同じ操作
- iPhone: Safari → 「ARで魔女を呼ぶ」→ Quick LookのAR表示 → 床に配置 → 撮影ボタン → 端末の保存・共有操作。
- Android: Chrome → 「ARで魔女を呼ぶ」→ Scene ViewerのAR表示 → 床に配置 → 撮影ボタンがあれば保存・共有。
- 撮影ボタンがない端末ではスクリーンショットを使ってください。端末・OSによって操作が異なります。
- 撮る人にスマホを渡し、魔女の横に並ぶと記念撮影できます。
- PCやAR非対応環境では3Dプレビューのみ。LINEなどのアプリ内ブラウザではSafari / Chromeで開き直してください。

## 仕様
ゴーストARの公開実装を確認し、同じレイアウト、3ステップ案内、撮影説明、OSビューア起動方式に合わせました。
ARモードは scene-viewer / quick-look。WebXRとページ内カメラ合成は使いません。
iPhone用USDZを固定ファイルとして同梱。写真はOSビューアで保存し、このWebアプリは写真を収集しません。
既存ゴーストARのソース・公開設定は変更していません。魔女の公開URLとQRはそのままです。

## モデル
元GLB assets/witch.glb（19,995,832バイト）は保持。
配信は assets/witch-mobile.glb（約4.0MB）と assets/witch.usdz（約16.8MB）。
ゴーストと同じ処理で高さ1m・底面接地・約6万面・テクスチャ最大1024pxに調整し、ポスターも生成。
編集前のモデルは元GLBに残っています。見え方は端末によって異なる場合があります。
変換ソースは tools/prepare_model.py（Blender 5用）。model-viewer 4.4.0とQRCode.js 1.0.0を同梱、ライセンスはvendor内。

## 更新
GitHub Desktopでこのリポジトリを開き、Commit → Push origin。
GitHub Pagesはmain / (root)、HTTPS。ビルド作業は不要です。
実機ARの撮影・保存・材質再現は未確認です。検証記録はVERIFICATION.md。
