const rainbows = document.getElementsByClassName('rainbow');
let initialHue = Math.floor(Math.random() * 360);
for (let rb of rainbows) {
    rb.hue = initialHue;
}

const updateRainbows = () => {
    for (let rb of rainbows) {
        rb.hue += 1;
        if (rb.hue > 360) rb.hue = 0;
        rb.style.backgroundColor = `hsla(${rb.hue}, 50%, 50%, ${rb.getAttribute('data-ralpha')}%)`;
    }
}
updateRainbows();
setInterval(updateRainbows, 100);