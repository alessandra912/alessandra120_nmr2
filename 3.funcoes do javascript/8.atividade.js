const readlineSync = require('readline-sync')

let valor_a = parseInt(readlineSync.question("Digite o valor a: "))
let valor_b = parseInt(readlineSync.question("Digite o valor b: "))
let valor_c = parseInt(readlineSync.question("Digite o valor c: "))

console.log(`\nValor a + valor b: ${valor_a + valor_b}`)
console.log(`Valor c: ${valor_c}`)

if (valor_a + valor_b > valor_c) {
    console.log('\nValor a + valor b é maior que valor c')
} else {
    console.log('\nValor a + valor b é menor que valor c')
}