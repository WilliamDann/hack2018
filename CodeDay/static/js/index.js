const button = document.getElementById('button');

button.addEventListener('focus', () => {
    button.classList.add('focused');
})