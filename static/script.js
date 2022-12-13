// get text area by id
const textArea = document.getElementById('user-note')
// console.log(textArea)

// Clear textarea value on click
const btn = document.getElementById('clear-text')
// console.log(btn)

btn.addEventListener('click', () => {
    // console.log(textArea.value);

    // Clear value
    textArea.value = ''
})