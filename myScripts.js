var doc = document;

var fileRun = doc.getElementById("run");
var fileRead = doc.getElementById("fileInput");
var content;
fileRead.addEventListener("change", (event) => {
    var file = event.target.files[0];
    var reader = new FileReader;
    reader.onload = (e) => {
        content = e.target.result;
    };
    reader.readAsText(file);

    content = file.text();
});
fileRun.addEventListener("click", function() {
    doc.getElementsByClassName("reportContent")[0].textContent = content;
})

var title = doc.getElementsByClassName("reportTitle");

for (var i = 0; i < title.length; i++) {
    title[i].addEventListener("click", function () {
        this.classList.toggle("active");
        var comment = this.nextElementSibling;
        if (comment.style.display === "block") {
            comment.style.display = "none";
        } else {
            comment.style.display = "block";
        }
    });
}