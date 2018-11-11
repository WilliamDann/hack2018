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
    button.classList.add('focused');
    setTimeout(() => {
        button.innerHTML = 'Make More Happy';
    }, 250);
    //fetch('/posts').then((res) => {
        //res.json().then((json) => {
            json = {
                "imagetitle": "I met a homeless guy on the pier at Venice Beach today. He was telling jokes for donations. I gave him $20 to tell me his three best. I was not disappointed nor will you.",
                "imageurl": {
                  "reddit_video": {
                    "dash_url": "https://v.redd.it/6zz13u4kqlx11/DASHPlaylist.mpd",
                    "duration": 48,
                    "fallback_url": "https://v.redd.it/6zz13u4kqlx11/DASH_9_6_M",
                    "height": 1080,
                    "hls_url": "https://v.redd.it/6zz13u4kqlx11/HLSPlaylist.m3u8",
                    "is_gif": false,
                    "scrubber_media_url": "https://v.redd.it/6zz13u4kqlx11/DASH_600_K",
                    "transcoding_status": "completed",
                    "width": 608
                  }
                },
                "newsdesc": "An American trucker passing through Ottawa treated a busload of Canadian veterans to dinner to honour their service.",
                "newstitle": "American trucker treats busload of Canadian veterans to dinner",
                "newsurl": "https://beta.ctvnews.ca/content/ctvnews/en/national/canada/2018/11/10/1_4171268.html",
                "quote": "30+ years as renters and my parents have finally bought a house!"
              };
            console.log(json);
            content.image.href = json.imageurl;
            content.imageTitle.innerHTML = json.imagetitle;
            content.quote.innerHTML = json.quote;
            content.newsTitle.innerText = json.newstitle;
            content.newsDesc.innerText = json.newsdesc;
            content.newsUrl.href = json.newsurl;
            button.classList.remove('focused');
        //});
    //}).catch(e => {
        //button.classList.remove('focused');
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

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.materialboxed');
    var instances = M.Materialbox.init(elems, {});
  });