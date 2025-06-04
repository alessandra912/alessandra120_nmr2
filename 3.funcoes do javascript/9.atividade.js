const readlineSync = require('readline-sync')

let numero = parseInt(readlineSync.question("Digite um número: "))

if (n => n % 2 === 0) {
    console.log(`\n${numero } é Par`)
} else {
    console.log(`\n${numero} é Impar`)
}
