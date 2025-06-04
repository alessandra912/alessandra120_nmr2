const readlineSync = require('readline-sync')

let dia_da_semana = parseInt(readlineSync.question('\nDigite um número para o dia da semana: '))

switch (dia_da_semana) {
    case 1:
        console.log('\nDomingo')
        break;
    case 2:
        console.log('\nSegunda-feira')
        break;
    case 3:
        console.log('\nTerça-feira')
        break
    case 4:
        console.log('\nQuarta-feira')
    case 5:
        console.log('\nQuinta-feira')
    case 6:
        console.log('\nSexta-feira')
    case 7:
        console.log('\nSábado')
    default:
        console.log('\nOpção inválida.')
        break
}