const hiddenLink = document.getElementById('hiddenLink');
const fake404 = document.getElementById('fake404');
const terminal = document.getElementById('terminal');
const input = document.getElementById('input');
const output = document.getElementById('output');

const validCommand = 'open-sesame';

hiddenLink.addEventListener('click', (e) => {
  e.preventDefault();
  fake404.style.display = 'none';
  terminal.style.display = 'block';
  input.focus();
  output.innerHTML += '<div>アクセス認証端末を起動中...</div>';
});

input.addEventListener('keydown', function (e) {
  if (e.key === 'Enter') {
    const command = input.value.trim();
    output.innerHTML += `<div>> ${command}</div>`;

    if (command === validCommand) {
      output.innerHTML += `<div>認証成功。ようこそ、隠された世界へ。</div>`;
      output.innerHTML += `<div style="margin-top:20px;">✨ Welcome to the Hidden World! ✨</div>`;
      input.style.display = 'none';
    } else {
      output.innerHTML += `<div>認証失敗。コマンドが違います。</div>`;
    }

    input.value = '';
    window.scrollTo(0, document.body.scrollHeight);
  }
});
