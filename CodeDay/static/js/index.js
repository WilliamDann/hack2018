const button = document.getElementById('main-button');

button.addEventListener('click', () => {
    button.style.top = '600px';
    setTimeout(() => {
        button.innerHTML = 'Make More Happy';
    }, 400);
});