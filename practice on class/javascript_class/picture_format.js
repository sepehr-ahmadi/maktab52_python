
function resize(x) {
    document.getElementById("flower_image").style.width = x + '%';
}
function blur_fig() {
    if (document.getElementById('blur').checked) {
        document.getElementById("flower_image").style.filter = "blur(4px)";
    } else {
        document.getElementById("flower_image").style.filter = "blur(0)";
    }

}
function brightness_fig() {
    if (document.getElementById('brightness').checked) {
        document.getElementById("flower_image").style.filter = "brightness(1.25)";
    } else {
        document.getElementById("flower_image").style.filter = "brightness(1)";
    }

}
function contrast_fig() {
    if (document.getElementById('contrast').checked) {
        document.getElementById("flower_image").style.filter = "contrast(1.5)";
    } else {
        document.getElementById("flower_image").style.filter = "contrast(1)";
    }

}