const readlineSync = require('readline-sync')

let idade = parseInt(readlineSync.question("\nDigite sua idade: "))

if (idade < 16) {
    console.log('\nNão podem votar.')
} else if ( idade <= 17)
    console.log('\nVoto opcional.') 
    else if (idade > 65) {
        console.log('\nNão são obrigados a votar.')
    } else {
        console.log('\nVoto obrigatório.')
    }