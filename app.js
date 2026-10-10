const viewer = document.querySelector('#witch');
const status = document.querySelector('#status');
const retry = document.querySelector('#retry');
viewer.addEventListener('progress', e => {
  document.querySelector('#progress').textContent = `モデルを読み込み中… ${Math.round(e.detail.totalProgress * 100)}%`;
});
viewer.addEventListener('load', () => {
  viewer.classList.add('loaded'); retry.hidden = true;
  status.textContent = viewer.canActivateAR ? '読み込み完了。ARボタンから魔女を呼び出せます。' : '読み込み完了。指で回転・拡大できます。ARは対応スマホで開いてください。';
});
viewer.addEventListener('error', () => {
  status.textContent = 'モデルを読み込めませんでした。通信状態を確認して再読み込みしてください。';
  retry.hidden = false;
});
viewer.addEventListener('ar-status', e => {
  if (e.detail.status === 'failed') status.textContent = 'ARを開始できませんでした。対応端末・カメラ許可を確認し、Safari／Chromeで開き直してください。';
  if (e.detail.status === 'session-started') status.textContent = '床に向けてスマホをゆっくり動かしてください。';
});
retry.addEventListener('click', () => location.reload());
document.querySelector('#rotation').addEventListener('click', e => {
  viewer.autoRotate = !viewer.autoRotate;
  e.target.textContent = viewer.autoRotate ? '自動回転を止める' : '自動回転する';
});
setTimeout(() => {
  if (!customElements.get('model-viewer')) {
    status.textContent = '3D表示機能を読み込めませんでした。ページを再読み込みしてください。'; retry.hidden = false;
  }
}, 15000);
const url = new URL(location.href); url.search = ''; url.hash = '';
if (url.protocol === 'https:') {
  const link = document.querySelector('#page-url'); link.href = url.href; link.textContent = url.href;
  new QRCode(document.querySelector('#qr'), {text:url.href,width:220,height:220,correctLevel:QRCode.CorrectLevel.M});
  document.querySelector('#qr-status').textContent = 'スマホのカメラで読み取ってください。';
  const canvas = document.querySelector('#qr canvas');
  const printable = document.createElement('canvas'); printable.width = printable.height = 268;
  const context = printable.getContext('2d'); context.fillStyle = '#fff'; context.fillRect(0, 0, 268, 268);
  context.drawImage(canvas, 24, 24);
  const download = document.querySelector('#download'); download.href = printable.toDataURL('image/png'); download.hidden = false;
  const copy = document.querySelector('#copy'); copy.hidden = false;
  copy.addEventListener('click', async () => {try {await navigator.clipboard.writeText(url.href);copy.textContent='コピーしました';}catch{copy.textContent='上のURLを長押ししてコピーしてください';}});
} else {
  document.querySelector('#qr-status').textContent = '公開後、HTTPSのURLで開くと配布用QRコードが表示されます。';
}
