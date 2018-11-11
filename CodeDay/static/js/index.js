const button = document.getElementById('main-button');
const mainbody = document.getElementById('mainbody');

const content = {
    quote: document.getElementById('quote'),
    image: document.getElementById('image'),
    imageTitle: document.getElementById('image-title'),
    imageUrl: document.getElementById('image-url'),
    newsTitle: document.getElementById('news-title'),
    newsDesc: document.getElementById('news-desc'),
    newsUrl: [document.getElementById('news-url'), document.getElementById('news-url-2')],
    newsImage: document.getElementById('news-image'),
};

button.addEventListener('click', () => {
    button.classList.add('focused');
    mainbody.style.transform = 'translateY(-86%)';
    setTimeout(() => {

        content.newsTitle.innerText = '';
        content.newsDesc.innerText = '';
        content.imageTitle.innerHTML = '';
    }, 400);
    setTimeout(() => {
    }, 250);
    fetch('/posts').then((res) => {
        res.json().then((json) => {
            console.log(json);
            content.quote.innerHTML = json.quote.text;

            let r = /https:\/\/imgur.com\/(.+)/;
            if (r.test(json.image.image))
                json.image.image = r.exec(json.image.image)[1];
            content.image.src = json.image.image;
            content.imageTitle.innerHTML = json.image.title;

            content.newsTitle.innerText = json.news.title;
            content.newsUrl[0].href = json.news.url;
            content.newsUrl[1].href = json.news.url;
            content.newsDesc.innerText = json.news.description;
            content.newsImage.src = json.news.image;
            button.classList.remove('focused');
            button.innerHTML = 'Make More Happy';
            mainbody.style.transform = 'translateY(0)';
        });
    }).catch(e => {
        button.classList.remove('focused');
    });
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

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.materialboxed');
    var instances = M.Materialbox.init(elems, {});
});