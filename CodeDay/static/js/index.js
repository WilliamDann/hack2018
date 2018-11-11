const button = document.getElementById('main-button');

<<<<<<< HEAD
button.addEventListener('focus', () => {
    button.classList.add('focused');
    button.classList.add('ng-hide');

})
=======
button.addEventListener('click', () => {
    button.style.top = '600px';
    setTimeout(() => {
        button.innerHTML = 'Make More Happy';
    }, 400);
});
>>>>>>> front_end
