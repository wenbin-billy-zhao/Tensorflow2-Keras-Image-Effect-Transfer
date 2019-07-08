
// Pull data and place into an object
var data
async function pullData() {
    const url = `/art_data`;
    data = await d3.json(url);
    console.log(data);

const artData = data

var version
// if info passed through form, hide options
version = document.getElementById("version");
version.innerHTML = version.innerText || version.textContent;
if (version.innerHTML) {

var contentPath;
var stylePath;
var quality;

    quality = document.getElementById("iterations");
    quality.innerHTML = quality.innerText || quality.textContent;
    contentPath = document.getElementById("content-path");
    contentPath.innerHTML = contentPath.innerText || contentPath.textContent;
    stylePath = document.getElementById("style-path")
    stylePath.innerHTML = stylePath.innerText || stylePath.textContent;
    // best_img
    best = document.getElementById("best");
    best.innerHTML = best.innerText || best.textContent;
    console.log(quality.innerHTML)
    console.log(contentPath.innerHTML)
    console.log(stylePath.innerHTML)
    console.log("running update")

    document.getElementById("content-place-holder").src=contentPath.innerHTML;
    document.getElementById("style-place-holder").src=stylePath.innerHTML;
    document.getElementById("best_img").src=best.innerHTML;
    document.getElementById("form_row").style.display = version.innerHTML;
    document.getElementById("carouselExampleIndicators").style.display = version.innerHTML;
    document.getElementById("cool-content-h2").removeAttribute("hidden")
    document.getElementById("cool-content").removeAttribute("hidden")
    document.getElementById("style_title").removeAttribute("hidden")
    document.getElementById("h2_result").removeAttribute("hidden")
    document.getElementById("h5_result").removeAttribute("hidden")
    document.getElementById("form_row_submit").style.display = version.innerHTML;
    

    console.log(version.innerHTML)


    if (quality.innerHTML == "10") {
        document.getElementById("low").removeAttribute("hidden")
    }
    else if (quality.innerHTML == "100") {
        document.getElementById("moderate").removeAttribute("hidden")
    }
    else {
        document.getElementById("high").removeAttribute("hidden")
    };
}

// read data into the table

// manipulate the array
var art_arrays = []
var art_pieces = []
for (i = 0; i < artData.artist.length; i++) {
    artArray = [];
    artPiece = []
    artArray.push(artData.artist[i]);
    artArray.push(artData.art_title[i]);
    artPiece.push(artData.art_image[i]);
    console.log(artData.artist[i]);
    art_arrays.push(artArray);
    art_pieces.push(artPiece)
};
console.log(art_arrays);

const tbody = d3.select("tbody");
// const tbody = metadata.append("tbody");
var counter = 0;
var counter2 = 0
    //  append to the table using a function to loop through all data
    art_arrays.forEach((product) =>{
    row = tbody.append("tr");
    row.attr("class", "clickable-row")
    row.attr("onClick", "styleSelect(this.id);")
    for (key in product){
        counter = counter + 1
        const cell = row.append("td");
        
        cell.text(product[key]);
        cell.attr('id', product[key]);
        if (counter==2) {
            cell.append("br")
            const style_select = cell.append("input")
            style_select.attr("type", "radio")
            style_select.attr("name", "style-library")
            style_select.attr("onclick", "styleSelect()")
            const img = cell.append("img")
            img.attr('src', art_pieces[counter2])
            row.attr("id", art_pieces[counter2])
            style_select.attr("id", art_pieces[counter2])
            counter2 = counter2 + 1
            counter = 0
        }
    };
});
}


function styleSelect(link){
    document.getElementById("style-library-selected").value=link;
    console.log(link)
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


// -------------------------------------------------------------------------

// onclick of 'Lets Begin'
// const run_submit = d3.select("run_submit");

// run_submit.on("click", async function(){
//     // Prevent the page from refreshing
//     d3.event.preventDefault();

//     document.getElementById("form_row").attr("hidden", "True")
// })
