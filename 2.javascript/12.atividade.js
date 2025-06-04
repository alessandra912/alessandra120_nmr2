// npm install readlinesync

const readline = require('readline-sync')

soma = 0
let nota = 0

for (let i=1; i <= 2; i++) {
    do {
        nota = readline.questionFloat("Digite o um número: ")
    } while (nota < 0 || nota > 10)
    soma += nota
}

media = soma / 2

console.log(`Média ${media}`)