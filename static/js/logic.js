// display image when selected
// --------------------------------------------------------------------------
// style image
function readURLstyle(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#style-image')
                .attr('src', e.target.result)
                .width(150)
                .height(200);
        };
        // document.getElementById("style-place-holder").src="";
        reader.readAsDataURL(input.files[0]);
    }
}
// content image
function readURLcontent(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#content-image')
                .attr('src', e.target.result)
                .width(150)
                .height(200);
        };
        // document.getElementById("content-place-holder").src="";
        reader.readAsDataURL(input.files[0]);
    }
}
// --------------------------------------------------------------------------

// upon launching of index.html
var contentPath;
var stylePath;
var quality;
function update() {
    quality = document.getElementById("iterations");
    quality.innerHTML = quality.innerText || quality.textContent;
    contentPath = document.getElementById("content-path");
    contentPath.innerHTML = contentPath.innerText || contentPath.textContent;
    stylePath = document.getElementById("style-path")
    stylePath.innerHTML = stylePath.innerText || stylePath.textContent;
    console.log(quality.innerHTML)
    console.log(contentPath.innerHTML)
    console.log(stylePath.innerHTML)
    console.log("running update")

    document.getElementById("content-place-holder").src=contentPath.innerHTML;
    document.getElementById("style-place-holder").src=stylePath.innerHTML;

    if (quality.innerHTML == "10") {
        document.getElementById("low").removeAttribute("hidden")
    }
    else if (quality.innerHTML == "100") {
        document.getElementById("moderate").removeAttribute("hidden")
    }
    else {
        document.getElementById("high").removeAttribute("hidden")
    }
}
// --------------------------------------------------------------------------