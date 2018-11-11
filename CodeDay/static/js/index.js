const button = document.getElementById('main-button');

const content = {
    quote: document.getElementById('quote'),
    image: document.getElementById('image'),
    imageTitle: document.getElementById('image-title'),
    imageUrl: document.getElementById('image-url'),
    newsTitle: document.getElementById('news-title'),
    newsDesc: document.getElementById('news-desc'),
    newsUrl: document.getElementById('news-url'),
};

button.addEventListener('click', () => {
    setTimeout(() => {
        button.innerHTML = 'Make More Happy';
    }, 250);
    fetch('/posts').then((res) => {
        res.json().then((json) => {
            console.log(json);
            content.image.href = json.imageurl;
            content.imageTitle.innerHTML = json.imagetitle;
            content.quote.innerHTML = json.quote;
            content.newsTitle.innerText = json.newstitle;
            content.newsDesc.innerText = json.newsdesc;
            content.newsUrl.href = json.newsurl;
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

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.materialboxed');
    var instances = M.Materialbox.init(elems, {});
  });