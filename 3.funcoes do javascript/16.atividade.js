const readline = require('readline-sync')

const listaDeNumeros = []

console.log('\n== Lista de números ==')
for (let i = 1; i <= 5; i++) {
    numeros = readline.questionInt(`Digite o ${i}º numero: `)
    listaDeNumeros.push(numeros)
}

const negativos = listaDeNumeros.filter(n => n < 0)
const positivos = listaDeNumeros.filter(n => n > 0).reduce((soma, total) => soma + total)
// const somaPositivos = positivos.reduce((soma, total) => soma + total, 0)

console.log(`\nNúmeros negativos: ${negativos}`)
console.log(`Soma de números positivos: ${positivos}`)
