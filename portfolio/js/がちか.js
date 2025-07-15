const text = document.querySelector('#text');
const light = document.querySelector('#light');

document.addEventListener('mousemove', function (event) {
  // マウスの動きに合わせて、要素(light)の位置を動かす
  const mouseX = event.clientX;
  const mouseY = event.clientY;
  light.style.left = mouseX + 'px';
  light.style.top = mouseY + 'px';

  const distanceX = mouseX - text.offsetLeft - text.offsetWidth / 2;
  const distanceY = mouseY - text.offsetTop - text.offsetHeight / 2;

  // 影の作成
  let newShadow = '';

  // 回数分box-shadowを追加する。
  for (let i = 0; i < 200; i++) {
    const shadowX = -distanceX * (i / 200);
    const shadowY = -distanceY * (i / 200);
    const opacity = 1 - i / 100;
    newShadow +=
      (newShadow ? ',' : '') + shadowX + 'px ' + shadowY + 'px 0 rgba(33,33,33,' + opacity + ')';
  }

  text.style.textShadow = newShadow;
});
