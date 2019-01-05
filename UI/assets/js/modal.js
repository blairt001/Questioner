// javascript modal
var modal = document.getElementById('deleteMeetupModal');
var modal2 = document.getElementById('addTagModal');
var modal3 = document.getElementById('addImageModal');
var modal4 = document.getElementById('createMeetupModal');

var btn = document.getElementById("deleteMeetupBtn");
var btn2 = document.getElementById("addTagBtn");
var btn3 = document.getElementById("addImageBtn");
var btn4 = document.getElementById("createMeetupBtn");

var span = document.getElementById("close-1");
var span2 = document.getElementById("close-2");
var span3 = document.getElementById("close-3");
var span4 = document.getElementById("close-4");

btn.onclick = function() {
  modal.style.display = "block";
}
btn2.onclick = function() {
  modal2.style.display = "block";
}
btn3.onclick = function() {
  modal3.style.display = "block";
}
btn4.onclick = function() {
  modal4.style.display = "block";
}
span.onclick = function() {
  modal.style.display = "none";
}
span2.onclick = function() {
  modal2.style.display = "none";
}
span3.onclick = function() {
  modal3.style.display = "none";
}
span4.onclick = function() {
  modal4.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
