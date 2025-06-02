// Arrow function
const somar = (a, b) => {
    return a + b
}

// Arrow function
const subtrair = (a, b) => a - b
const multiplicar = (a, b) => a * b
const dividir = (a, b) => a / b

// Chamando uma função
const soma = somar(2,3)
const subtracao = subtrair(2,3)
const multiplicacao = multiplicar(2,3)
const divisao = dividir(2,3)

// Exibir resultado
console.log(`Soma: ${soma}`)
console.log(`Subtrair: ${subtracao}`)
console.log(`Multiplicar: ${multiplicacao}`)
console.log(`Dividir: ${divisao}`)