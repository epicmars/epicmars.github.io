function init() {

    // highlight
    hljs.initHighlightingOnLoad();
    // fancybox
    var imgs = document.querySelectorAll("article img");
    imgs.forEach(img => {
        var a = document.createElement('a');
        a.setAttribute('href', img.src);
        a.setAttribute('data-fancybox', 'gallery');
        replaced = img.parentElement.replaceChild(a, img);
        a.appendChild(replaced);
    });
    // fastclick
    FastClick.attach(document.body);
}

if ('addEventListener' in document) {
    document.addEventListener('DOMContentLoaded', init, false);
}