const button = document.getElementById('main-button');

button.addEventListener('click', () => {
    setTimeout(() => {
        button.innerHTML = 'Make More Happy';
    }, 250);
    fetch('/posts').then((res) => {
        res.json().then((json) => {
            console.log(json);
        });
    })
});
let updateNight = () => {
    let t = new Date();
    if (t.getHours() > 19 || t.getHours() < 5) {
        if (document.body.className !== 'night')
            document.body.className = 'night';
    } else {
        if (document.body.className === 'night')
            document.body.className = '';

    }
};
updateNight();

setInterval(updateNight, 5000);