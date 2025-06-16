const inputsNotas = document.querySelectorAll('input.nota');
const listaNotas = document.getElementById('listaNotas');
const mediaFinal = document.getElementById('mediaFinal');

function atualizarNotasEMedia() {
  let notas = [];

  inputsNotas.forEach(input => {
    const val = parseFloat(input.value);
    if (!isNaN(val) && val >= 0 && val <= 10) {
      notas.push(val);
    }
  });

  listaNotas.innerHTML = '';

  if (notas.length === 0) {
    listaNotas.innerHTML = '<li>Digite uma nota menor que 10.</li>';
    mediaFinal.textContent = '0.0';
    return;
  }

  notas.forEach((nota, i) => {
    const li = document.createElement('li');
    li.textContent = `Nota ${i + 1}: ${nota.toFixed(2)}`;
    listaNotas.appendChild(li);
  });

  const soma = notas.reduce((acc, n) => acc + n, 0);
  const media = soma / notas.length;

  mediaFinal.textContent = media.toFixed(2);
}

// Atualiza a cada digitação
inputsNotas.forEach(input => {
  input.addEventListener('input', atualizarNotasEMedia);
});