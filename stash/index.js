const button = document.getElementById('button');

button.addEventListener('click', async () => {
    if (button.className.includes('focused')) return;
    button.classList.add('focused');
    try {
        let post = await fetch('/posts');
        post = JSON.parse(post);
    } catch {
        button.classList.add('error');
        button.innerText = ':(';
        button.style.backgroundColor = '#eb2f06';
    }
});


document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.materialboxed');
    var instances = M.Materialbox.init(elems, {});
});