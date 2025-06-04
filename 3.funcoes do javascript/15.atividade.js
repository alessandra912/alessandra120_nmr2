const readline = require('readline-sync')

const listaDeNumeros = []

console.log('\n== Lista de números ==')
for (let i = 1; i <= 6; i++) {
    numeros = readline.questionInt(`Digite o ${i}º numero: `)
    listaDeNumeros.push(numeros)
}

const pares = listaDeNumeros.filter(n => n % 2 === 0)
const impares = listaDeNumeros.filter(n => n % 2 !== 0)

if (pares == 1 || impares == 1) {
console.log(`\n${pares} é par`)
console.log(`${impares} é impar`)
} else {
    console.log(`\n${pares} são pares`)
    console.log(`${impares} são impares`)
}
