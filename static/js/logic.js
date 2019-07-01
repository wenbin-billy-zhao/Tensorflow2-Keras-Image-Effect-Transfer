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

// save images, pull, and update html page

// var submit = d3.select("#submit");

// submit.on("click", async function() {
//     d3.event.preventDefault();
//     // const contentFile = d3.select("#keywords");
//     // const styleFile = d3.select("#keywords");
//     // const quality = d3.select("#keywords");
// )}