const button = document.getElementById('main-button');
const mainbody = document.getElementById('mainbody');

var content = {
    quote: document.getElementById('quote'),
    image: document.getElementById('image'),
    embed: document.getElementById('embed'),
    imageTitle: document.getElementById('image-title'),
    imageUrl: document.getElementById('image-url'),
    newsTitle: document.getElementById('news-title'),
    newsDesc: document.getElementById('news-desc'),
    newsUrl: [document.getElementById('news-url'), document.getElementById('news-url-2')],
    newsImage: document.getElementById('news-image'),
    click: {
        image: document.getElementById('hover-image-click'),
        quote: document.getElementById('hover-quote-click')
    }
};

button.addEventListener('click', () => {
    window.scrollTo(0, 0);
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
            content.click.quote.href = json.quote.reddit_url;

            if (json.image.image.includes('imgur.com') && !json.image.image.includes('i.imgur.com')) {
                content.embed.src = json.image.image + "/enbed";
                content.embed.style.display = 'block';
                content.image.style.display = 'none';
            } else {
                content.image.src = json.image.image;
                content.embed.style.display = 'none';
                content.image.style.display = 'block';
            }
            let r = /https:\/\/imgur.com\/(.+)/;
            if (r.test(json.image.image))
                json.image.image = r.exec(json.image.image)[1];
            content.image.src = json.image.image;
            content.imageTitle.innerHTML = json.image.title;
            content.click.image.href = json.image.reddit_url;
            
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