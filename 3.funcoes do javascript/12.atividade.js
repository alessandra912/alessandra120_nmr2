const readlineSync = require('readline-sync')

let numero = parseInt(readlineSync.question("\nDigite um número: "))

if (numero < 0) {
    console.log(`\n${numero} é um número negativo`)
} else {
    console.log(`\n${numero} é um múmero positivo`)
}