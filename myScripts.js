var doc = document;

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