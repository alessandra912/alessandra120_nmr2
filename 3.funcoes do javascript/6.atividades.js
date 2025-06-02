const readlineSync = require('readline-sync')

let idade = parseInt(readlineSync.question("Digite sua idade: "))

if (idade < 16) {
    console.log('Não podem votar.')
} else if ( idade <= 17)
    console.log('Voto opcional.') 
    else if (idade > 65) {
        console.log('Não são obrigados a votar.')
    } else {
        console.log('Voto obrigatório')
    }