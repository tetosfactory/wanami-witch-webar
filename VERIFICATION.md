# 検証記録

確認日: 2026-10-11 (日本時間)

- ローカル元GLBへアクセス成功。コピーと元ファイルのSHA-256一致。
- SHA-256: CAB67BAF63B3E325205601D393F88AC292AD30E3444FE29676E6E5F2FBFFFBC9
- GLBヘッダー: glTF / version 2 / 宣言サイズ19,995,832バイトと実サイズ一致。
- モデル1・材質1・テクスチャ3。外部URIなし。POSITION bounds: (-0.388336,0,-0.277939) ～ (0.388336,1,0.277939)。
- extensionsUsed: KHR_materials_volume, FB_ngon_encoding。特殊材質のAR側再現は未確認。
- model-viewer 4.4.0 / QRCode.js 1.0.0 を同梱。ライセンス添付。
- app.js の構文チェック成功。
- ローカルHTTP 200。ブラウザでGLB読み込み完了とテクスチャ付き魔女の表示を確認。
- 390px幅で横にはみ出さないこと、自動回転停止ボタンの動作を確認。
- スマホ実機での床認識・カメラ・Android AR・iOS Quick Look変換結果は未確認。
- 公開URLとQRの確認結果はPUBLICATION.mdに記録。
- HTTPS公開ページでGLB読み込み完了とQR生成を確認。
- 配布用QRは984×984px、白い余白4モジュール。独立したQRデコーダーで公開URLとの一致を確認。
