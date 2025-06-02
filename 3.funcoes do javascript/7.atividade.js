const readlineSync = require('readline-sync')

let valor_a = parseInt(readlineSync.question("Digite o valor a: "))
let valor_b = parseInt(readlineSync.question("Digite o valor b: "))

const somar(valor_a + valor_b) = valor_c

if (valor_a == valor_b) {
    valor_c = somar(valor_a + valor_b)
} else {
    valor_c = multiplicar(valor_a * valor_b)
}

console.log(`Valor C: ${valor_c}`)