/*

const nothing = () => {}

console.log('start')

setTimeout(nothing, 3000)
console.log('end')



function sleep_3s(){
  setTimeout(() => {
    console.log('Wake up js')
  }, 3000)
}

console.log('start sleeping')
sleep_3s()
console.log('end program')


function first() {
  console.log('first')
}

function second(){
  console.log('second')
}

function third(){
  console.log('third')
}

first()
setTimeout(second, 0)
third()
*/

console.log('hello')

setTimeout(function cb1() {
  console.log('cb1')
}, 5000)
console.log('byebye')