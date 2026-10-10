# 検証記録
確認日: 2026-10-11（日本時間）

## ゴーストARに合わせた更新
- 参照: tetosfactory/wanami-ghost-ar の index.html / app.js / style.css / tools/prepare_model.py（2026-10-11取得）。
- OSのScene Viewer / Quick Look起動、写真保存、スクリーンショット代替、対応端末案内、画面構成を一致させた。
- ページ内の独自カメラ撮影は含めない。WebXRはARモードから外した。
- 元GLBを保持し、モバイル配信用GLBと固定USDZ、ポスターを生成。
- model-viewer 4.4.0は既存の魔女プロジェクトのバージョンを保持（ゴーストは4.1.0）。
- 元GLB SHA-256: CAB67BAF63B3E325205601D393F88AC292AD30E3444FE29676E6E5F2FBFFFBC9
- 変換: 高さ1m / 6万面 / 最大1024pxテクスチャ / アニメーションなし。
- GLB: 4,039,744バイト、USDZ: 16,829,994バイト。詳細はmodel-report.json。
- USDZはPNGテクスチャを同梱し、無圧縮・64バイト境界・参照画像の存在を検証。
- app.js構文確認。ブラウザで変換後GLBが読み込まれ、撮影案内と非対応PCの状態表示を確認。
- 既存QRは同じ公開URLのまま。白い余白4モジュール、984×984px、デコーダーでURL一致を確認済み。
- スマホ実機での床認識・撮影・保存、USDZの材質再現は未検証。
