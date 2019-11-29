
$(function () { objectFitImages() });

$('.navbar-nav>li>a').on('click', function(){
    $('.navbar-collapse').collapse('hide');
});


window.onresize = function(event) {
        // window.alert(window.location.hash);
    var x = window.location.hash;
    if(x != ""){
      window.location.replace(window.location.hash)
    }

};

var read=document.getElementById("read-mode");
 var blog=document.getElementById("blog-content");
read.addEventListener("click", ModeChange);
function ModeChange(){
  if (read.checked== true){

    blog.classList.add("text-light","bg-black");
}else {
      blog.classList.remove("text-light","bg-black")
  }
};
