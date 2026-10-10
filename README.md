# わなみフェス 魔女 WebAR

公開URL: https://tetosfactory.github.io/wanami-witch-webar/

配布用QR: [QR画像](qr/wanami-witch-qr.png)

指定GLBを使った独立した静的WebARアプリ。ビルド不要。元ファイルや既存プロジェクトは変更していません。

## 操作
1. 公開ページのQRをスマホのカメラで読み取る。
2. iPhoneはSafari、AndroidはChromeで開く。
3. 読み込み後「魔女をARで呼び出す」を押す。カメラ利用を許可し、明るい場所で床に向けてゆっくり動かす。
4. 指で位置・大きさを調整。終了は端末の戻る／閉じる。

## 端末の違い
- Android: WebXRを優先し、Scene Viewerへフォールバック。ARCore対応やGoogle Play開発者サービス(AR)など端末側の条件があります。
- iOS: Quick Look用USDZをmodel-viewerが操作時に自動生成。別USDZは未添付。変換に時間がかかる場合があり、特殊な材質は見え方が変わることがあります。Safariを推奨。
- PC・非対応端末: 3D回転・拡大表示。実機AR・iOS変換結果は別途確認が必要です。
- QRはページへのリンクです。画像認識マーカーではありません。

## 公開
GitHub Desktopで新規リポジトリを公開した後、GitHubのSettings → Pages → Deploy from a branch → main / (root) → Save。
HTTPSが有効になった公開ページを開くと、そのページ自身のURLのQRをローカル生成できます。QRに外部生成サービスは使いません。

## モデル
assets/witch.glb は指定GLBのコピー。glTF 2.0 / Tripo生成 / 約20MB / メッシュ1 / マテリアル1 / テクスチャ3 / アニメーションなし / 高さ約1m。テクスチャ内包。元の衣装・形状を保持。
モデルの権利を変更するライセンスは付与していません。

## 依存と検証
公式model-viewerとQRCode.jsをvendorに固定して同梱。バージョンと検証結果はVERIFICATION.md参照。
公式AR仕様: https://modelviewer.dev/docs/#entrydocs-augmentedreality-attributes-ar-modes
