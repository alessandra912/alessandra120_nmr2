function iniciarContagem() {
    const input = document.getElementById('numeroInput');
    let numero = parseInt(input.value);
    
    const resultado = document.getElementById('resultado');

    if (isNaN(numero) || numero < 1) {
        resultado.textContent = 'Digite um número válido maior que 0.';
        return;
    }

    resultado.textContent = '';

    const intervalo = setInterval(() => {
        resultado.textContent = `Contagem: ${numero}`;
        numero--;

        if (numero < 1) {
            clearInterval(intervalo);
            setTimeout(() => {
                resultado.textContent = 'Contagem finalizada!';
            }, 1000);
        }
    }, 1000);
}

const gerarBotao = document.getElementById('gerarBotao')
gerarBotao.addEventListener('click', )
// document.getElementById('iniciarBotao').addEventListener('click', iniciarContagem);