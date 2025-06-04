const readlineSync = require('readline-sync')

let valor_a = parseInt(readlineSync.question("\nDigite o valor a: "))
let valor_b = parseInt(readlineSync.question("Digite o valor b: "))

if (valor_a == valor_b) {
    valor_c = valor_a + valor_b
} else {
    valor_c = valor_a * valor_b
}

console.log(`\nValor C: ${valor_c}`)