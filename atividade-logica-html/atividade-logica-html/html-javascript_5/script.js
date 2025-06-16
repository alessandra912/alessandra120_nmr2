const inputsNotas = document.querySelectorAll('input.nota');
const listaNotas = document.getElementById('listaNotas');
const mediaNumero = document.getElementById('mediaNumero');
const statusAluno = document.getElementById('statusAluno');

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
    listaNotas.innerHTML = '<li>Escreva uma nota menor que 10.</li>';
    mediaNumero.textContent = '0.00';
    mediaNumero.className = '';
    statusAluno.textContent = '';
    statusAluno.className = '';
    return;
  }

  notas.forEach((nota, i) => {
    const li = document.createElement('li');
    li.textContent = `Nota ${i + 1}: ${nota.toFixed(2)}`;
    listaNotas.appendChild(li);
  });

  const soma = notas.reduce((acc, n) => acc + n, 0);
  const media = soma / notas.length;

  mediaNumero.textContent = media.toFixed(2);
  mediaNumero.className = '';  // limpa classes anteriores
  statusAluno.textContent = '';
  statusAluno.className = '';

  // Define status e classes de cor separadas
  let status = '';
  let classeMedia = '';
  let classeStatus = '';

  if (media >= 7) {
    status = 'Aluno Aprovado!';
    classeMedia = 'media-aprovado';
    classeStatus = 'status-aprovado';
  } else if (media < 4) {
    status = 'Aluno Reprovado!';
    classeMedia = 'media-reprovado';
    classeStatus = 'status-reprovado';
  } else {
    status = 'Aluno em Recuperação!';
    classeMedia = 'media-recuperacao';
    classeStatus = 'status-recuperacao';
  }

  mediaNumero.classList.add(classeMedia);
  statusAluno.textContent = status;
  statusAluno.classList.add(classeStatus);
}

// Atualiza ao digitar
inputsNotas.forEach(input => {
  input.addEventListener('input', atualizarNotasEMedia);
});

// Inicializa na carga da página
atualizarNotasEMedia();