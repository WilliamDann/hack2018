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

var ind = 0;
var c = [
    {
        "image": {
            "image": "https://i.redd.it/grprd3yeecx11.jpg",
            "reddit_url": "https://redd.it/9vmk23",
            "title": "[Image] Just be"
        },
        "news": {
            "description": "Nepal is one of 13 tiger-range countries striving to double the world\u2019s tiger population by 2022. ",
            "image": "https://video-images.vice.com/articles/5ba913364cd7cf00064aba03/lede/1537807352410-Bardia-NP2.jpeg?crop=1xw:0.7303427419354839xh;center,center&resize=1200:*",
            "reddit_url": "https://redd.it/9l7wu1",
            "title": "The Tiger Population in Nepal Has Nearly Doubled Since 2009 Because Conservation Efforts Work",
            "url": "https://motherboard.vice.com/en_us/article/7xjxdd/the-tiger-population-in-nepal-has-nearly-doubled-since-2009-because-conservation-efforts-work"
        },
        "quote": {
            "reddit_url": "https://redd.it/9tduk1",
            "text": "Start something now not after!"
        }
    },
    {
        "image": {
            "image": "https://i.redd.it/grhsgnvidqx11.jpg",
            "reddit_url": "https://redd.it/9w58a8",
            "title": "Newest member of the team."
        },
        "news": {
            "description": "A homeless man, who goes by the name Adam, sold an old art print he found in a dumpster to an antiques store for $20. But when shop's owner Alex Archbold realized it was worth much more than that, he set out to find Adam, and give him his fair share.",
            "image": "https://i.cbc.ca/1.4900125.1541800552!/fileImage/httpImage/image.jpg_gen/derivatives/16x9_620/edmonton-antique.jpg",
            "reddit_url": "https://redd.it/9vztgu",
            "title": "Homeless Edmonton man discovers rare Disney art in 'ratty old plastic bag' is worth thousands | CBC Radio",
            "url": "https://www.cbc.ca/radio/asithappens/as-it-happens-friday-edition-1.4899122/homeless-edmonton-man-discovers-rare-disney-art-in-ratty-old-plastic-bag-is-worth-thousands-1.4899486"
        },
        "quote": {
            "reddit_url": "https://redd.it/9v7yqx",
            "text": "Smile even through your tears, Be Strong even through your fears - Unknown"
        }
    },
    {
        "image": {
            "image": "https://i.redd.it/grprd3yeecx11.jpg",
            "reddit_url": "https://redd.it/9vmk23",
            "title": "[Image] Just be"
        },
        "news": {
            "description": "A bystander dubbed \u201cthe trolley man\u201d for taking on an armed terrorist with a shopping cart during the deadly terror attack in Melbourne says he is \u201cno hero\u201d as his story comes to light.",
            "image": "https://cdn.newsapi.com.au/image/v1/6416fed25888b1fd9434b06946539590?width=650",
            "reddit_url": "https://redd.it/9w06i0",
            "title": "GoFundMe set up for the hero \u201ctrolleyman\u201d, who thwarted a terrorist, has raised almost triple its original target in less than a day.",
            "url": "https://www.news.com.au/national/im-no-hero-trolley-man-recounts-moment-of-terror/news-story/6b6496e214615682b956359d879407ed"
        },
        "quote": {
            "reddit_url": "https://redd.it/9w3zbb",
            "text": " \"Fear and pain should be treated as signals not to close our eyes but to open them wider.\" - from Six pillars of self-esteem by Nathaniel Branden"
        }
    },
    {
        "image": {
            "image": "https://i.imgur.com/mx3ncIb.jpg",
            "reddit_url": "https://redd.it/9w045j",
            "title": "There'll always be a space for him in her heart"
        },
        "news": {
            "description": "Mayor Bill de Blasio called the achievement \"extraordinary\" on Monday while speaking at a graduation ceremony for newly sworn NYPD officers.",
            "image": "https://cdn.cnn.com/cnnnext/dam/assets/171101082938-ny-attack-police-super-tease.jpg",
            "reddit_url": "https://redd.it/9p228r",
            "title": "For the first time in 25 years New York City didn't have a single shooting over the weekend",
            "url": "https://www.cnn.com/2018/10/16/us/new-york-city-shootings-weekend-trnd/index.html"
        },
        "quote": {
            "reddit_url": "https://redd.it/9v6dkb",
            "text": "Nature is for humans not humans nature"
        }
    },
    {
        "image": {
            "image": "https://i.redd.it/yjyyb64pgnx11.jpg",
            "reddit_url": "https://redd.it/9w1ues",
            "title": "Today 25 years ago my mother adopted me!"
        },
        "news": {
            "description": "A new modification that brings artificial intelligence to Minecraft makes players better architects and AI better at recognizing images.",
            "image": "https://www.futurity.org/wp/wp-content/uploads/2018/11/minecraft-players_1600.jpg",
            "reddit_url": "https://redd.it/9w4ei4",
            "title": "A.I. teaches Minecraft players about architecture",
            "url": "https://www.futurity.org/artificial-intelligence-minecraft-1906842/"
        },
        "quote": {
            "reddit_url": "https://redd.it/9vhmor",
            "text": "Believe you can and you're halfway there. - Theodore Roosevelt"
        }
    }
];

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
    //fetch('/posts').then((res) => {
    //res.json().then((json) => {
    setTimeout(() => {
        json = c[ind];
        ind++;
        if (ind > c.length)
            ind = 0;
        content.quote.innerHTML = json.quote.text;
        content.click.quote.href = json.quote.reddit_url;

        if (json.image.image.includes('imgur.com') && !json.image.image.includes('i.imgur.com')) {
            content.embed.src = json.image.image + "/embed";
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
    }, 500);
    //}).catch(e => {
    //    button.classList.remove('focused');
    //});
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