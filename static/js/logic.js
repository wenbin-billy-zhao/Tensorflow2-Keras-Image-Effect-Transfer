
// Pull data and place into an object
var data
async function pullData() {
    const url = `/art_data`;
    data = await d3.json(url);
    console.log(data);

const artData = data

// read data into the table
var art_arrays = []
var art_pieces = []
for (i = 0; i < artData.artist.length; i++) {
    artArray = [];
    artPiece = []
    artArray.push(artData.artist[i]);
    artPiece.push(artData.art_image[i]);
    artArray.push(artData.art_title[i]);
    console.log(artData.artist[i]);
    art_arrays.push(artArray);
    art_pieces.push(artPiece)
};
console.log(art_arrays);


const tbody = d3.select("tbody");
// const tbody = metadata.append("tbody");


    //  append to the table using a function to loop through all data
    art_arrays.forEach((product) =>{
    row = tbody.append("tr");
    for (key in product){
        const cell = tbody.append("td");
        cell.text(product[key]);
    };
});
}

// --------------------------------------------------------------------------


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
};
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
};
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
};
// -------------------------------------------------------------------------