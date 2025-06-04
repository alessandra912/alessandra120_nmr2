const readline = require('readline-sync')

listaDeNotas = []

for (let i = 1; i <= 2; i++) {
    nota = readline.questionInt(`\nDigite a ${i}ª nota: `)
    listaDeNotas.push(nota)
}

soma = listaDeNotas.reduce((soma, total) => soma + total, 0)

quantidadedeNotas = listaDeNotas.length

console.log('\n== Notas ==')
listaDeNotas.forEach((nota, index) => console.log(`${++index}ª nota: ${nota}`))

media = soma / quantidadedeNotas
console.log(`\nMédia da soma das notas: ${media}`)