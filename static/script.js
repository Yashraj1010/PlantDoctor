const dropArea = document.getElementById("drop-area")
const inputFile = document.getElementById("input-file")
const imageView = document.getElementById("img-view")

var showDisease_data , vgg_result = "";


function uploadImage(){
    let imgLink  =  URL.createObjectURL(inputFile.files[0]);
    imageView.style.backgroundImage = `url(${imgLink})`;
    imageView.textContent = "";
    imageView.style.border = 0;
}

function updateRangeLabel(labelId,Text, value) {
    document.getElementById(labelId).innerHTML = `${Text} - <b style="color: red; font-size: 15px;" >${value}</b>`;
}

inputFile.addEventListener("change" , uploadImage);

dropArea.addEventListener("dragover" , function(e){
    e.preventDefault();
})
dropArea.addEventListener("drop" , function(e){
    e.preventDefault();
    inputFile.files = e.dataTransfer.files;
    uploadImage();
})

document.querySelector('#upload_btn').addEventListener('click', function() {
    //<--------------------Get NPK value-------------------->

    var k = document.getElementById("Potassium").value;
    var p = document.getElementById("Phosphorus").value;
    var n = document.getElementById("Nitrogen").value;
    var plant = document.getElementById("plantSelect").value;





    if (!inputFile.files[0] || k==0 || n==0 || p==0) {
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Check Image and NPK values",
            footer: "<b >Looks like you didn't uploaded any image..</b>"
        });
        return;
    }
    let formData = new FormData();
    let loading_div  = document.getElementById("loading_div");
    let hero_div = document.getElementById("hero")
    let result_div = document.getElementById("result");
    let npk_result_para = document.getElementById("npk_result_para");
    let npk_reslt_parent = document.getElementById("npk_reslt_parent");


    //<----------------------------------- Model div selection ------------------------->
    let cnn_id = document.getElementById("cnn_id");
    let vgg_id = document.getElementById("vgg_id");
    let densenet_id = document.getElementById("densenet_id");

    loading_div.style.visibility = "visible";
    hero_div.style.filter="blur(4px)";

    //<------------------------Get NPK and Plant Vlues------------------------->
    formData.append('file', inputFile.files[0]);
    formData.append('n', n);
    formData.append('p', p);
    formData.append('k', k);
    formData.append('plant', plant);

    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => new Promise(resolve => setTimeout(() => resolve(response), 10))) // Add a 2-second delay
    .then(response => response.json())
    .then(data => {
        console.log(data); // Handle the response data here
        let cnn_result = `<br> Prediction: <b>${data.cnn_class}</b><br>Confidence: <b>${data.cnn_confidence}</b>`;
        cnn_id.innerHTML = cnn_result;

        vgg_result = `<br> Prediction: <b>${data.vgg_class}</b><br>Confidence: <b>${data.vgg_confidence}</b>`;
        vgg_id.innerHTML = vgg_result;

        let densenet_result = `<br> Prediction: <b>${data.densenet_class}</b><br>Confidence: <b>${data.densenet_confidence}</b>`;
        densenet_id.innerHTML = densenet_result;

        npk_result_para.innerText = data.npk_result;
        showDisease_data = data.diseases_result;

        // Undo the changes
        loading_div.style.visibility = "hidden";
        hero_div.style.filter = "none";
        result_div.style.visibility="visible";
        npk_reslt_parent.style.visibility="visible";
    })
    .catch(error => {
        console.error('Error:', error);
        // Undo the changes
        loading_div.style.visibility = "hidden";
        hero_div.style.filter = "none";
        result_div.style.visibility="hidden";
    });
});

function showDisease(){
    Swal.fire({
        title: vgg_result,
        text: showDisease_data,
        imageUrl: "/static/navbar_logo.jpeg",
        imageWidth: 400,
        imageHeight: 200,
        imageAlt: "Diseases report"
      });
}