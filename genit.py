from gtts import gTTS
import random
import os
from shutil import rmtree

n = 100
name = "placid_cow"
random.seed(10)

try:
    rmtree(name)
except:
    pass

os.mkdir(name)
os.mkdir(name+"/sounds")

s = """<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>"""+name+""": Memory Game Admin</title>
  <link href="style.css" rel="stylesheet" type="text/css" />
</head>
<body>
  <div class="numcorrect">
    0
  </div>
  <div class="numwrong">
    0
  </div>
  <p padding-bottom: 10vh; margin-bottom: 10vh;>
    <br>
  </p>
  <p padding-bottom: 10vh; margin-bottom: 10vh;>
    <br>
  </p>
  <ul id="list1">\n"""

def getButton(words,first=False):
    fn = "'sounds/"+"_".join(words)+".mp3'"
    butex = " ".join(words)
    if(first):
        return('<li class="current" data-filename='+fn+'>'+butex+'</li>')
    return('<li data-filename='+fn+' >'+butex+'</li>')

nounlist = []
with open("myn.txt") as f:
    for line in f:
        nounlist.append(line.strip())

for i in range(n):
    words = random.sample(nounlist, 5)
    print(words)
    audio = gTTS(text=". ".join(words), lang="en", slow=True)
    audio.save(name+"/sounds/" + "_".join(words) + ".mp3")
    s += getButton(words,i==0)+"\n"

s += """\n</ul>
  <script src="script.js"></script>
</body>

</html>"""

with open(name+"/"+name+".html","w") as f:
    f.write(s)

s2 = """/* Removes the bullet points from the list */ 
ul{
  margin:0;
  padding:0;
}

/* Format the list items */
ul li{
  cursor:pointer;
  position:relative;
  padding:10px 8px 10px 30px;
  background:rgba(100, 150, 220, 0.685);
  font-size:20px;
  transition:0.2s;
} 

/* Changes the color of the list item when hovered over */

ul li:hover{
  background:rgb(125, 175, 240);
}


/* Formats the checked list item */
ul li.current{
  background:#337;
  color:#fff;
}

/*
ul li.current:hover{
  background:#777;
  color:#111;
}
*/

ul li.yes{
  background:#5B5;
  color:#141;
}

ul li.yes.current{
  background:#373;
  color:#fff;
}

ul li.no{
  background:#B55;
  color:#411;
}

ul li.no.current{
  background:#733;
  color:#fff;
}


/* Formats the header */
.header{
  background-color:#a7d3ecef;
  padding:20px 30px 50px;
  color:white;
  text-align:left;
}


input{
  font-size:22px;
  padding:2px;
}

/* Styles the Add button */
button{
  padding:2px;
  width:20vh;
  background:#d9d9d9;
  color:#555;
  float:left;
  text-align:center;
  font-size:22px;
  cursor:pointer;
  transition:0.3s;
  border-radius:0;
}

/* Changes the color when button is hovered over */
button:hover{
  background-color:rgb(203, 202, 204);
}


/* Formats the close button for each list item */
.close{
  position:absolute;
  right:0;
  top:0;
  padding:10px 16px 10px 16px;
}

/* Changes the style of the close button when hovered over */
.close:hover{
  background-color:#c90a3a;
  color:white;
}

.Y{
  float: right;
  padding:4px 8px 4px 8px;
  background:#5B5;
  color:#141;
}

.N{
  float: right;
  padding:4px 8px 4px 8px;
  background:#B55;
  color:#411;
}

.P{
  float: right;
  padding:4px 8px 4px 8px;
  background:#888;
  color:#000;
}

.C{
  float: right;
  padding:4px 8px 4px 8px;
  background:rgba(100, 150, 220, 0.685);
}

.Y:hover{
  background:#8F8;
  color:#000;
}

.N:hover{
  background:#F88;
  color:#000;
}

.P:hover{
  background:#BBB;
  color:#000;
}

.C:hover{
  background:rgb(150, 200, 255);
}

.numcorrect {
  display: block;
  position: fixed;
  top: 0px;
  left: 0px;
  width: 10vw;
  height: 5vh;
  z-index: 99;
  font-size: 3vh;
  border: none;
  outline: none;
  background-color: green;
  color: white;
  cursor: pointer;
  padding:8px 16px 4px 16px;
  border-radius: 1vh;
}

.numwrong {
  display: block;
  position: fixed;
  top: 0px;
  left: 20vw;
  width: 10vw;
  height: 5vh;
  z-index: 99;
  font-size: 3vh;
  border: none;
  outline: none;
  background-color: red;
  color: white;
  cursor: pointer;
  padding:8px 16px 4px 16px;
  border-radius: 1vh;
}"""

with open(name+"/style.css","w") as f:
    f.write(s2)

s3 = """function playAudio(url) {
  new Audio(url).play();
}


function createY(item) {
  var span = document.createElement("SPAN");
  var txt = document.createTextNode("Y"); //Unicode character for "X"
  span.className = "Y"; //needed for CSS access
  span.appendChild(txt);
  item.appendChild(span);
}

function createN(item) {
  var span = document.createElement("SPAN");
  var txt = document.createTextNode("N"); //Unicode character for "X"
  span.className = "N"; //needed for CSS access
  span.appendChild(txt);
  item.appendChild(span);
}

function createC(item) {
  var span = document.createElement("SPAN");
  var txt = document.createTextNode("C"); //Unicode character for "X"
  span.className = "C"; //needed for CSS access
  span.appendChild(txt);
  item.appendChild(span);
}

function createP(item) {
  var span = document.createElement("SPAN");
  var txt = document.createTextNode("P"); //Unicode character for "X"
  span.className = "P"; //needed for CSS access
  span.appendChild(txt);
  item.appendChild(span);
}

//Add an X at the end of each list item
var itemList = document.getElementsByTagName("LI");
var i;
for (i = 0; i < itemList.length; i++) {
  createC(itemList[i]);
  createN(itemList[i]);
  createY(itemList[i]);
  createP(itemList[i]);
  itemList[i].innerHTML = "" + (i + 1) + ":  " + itemList[i].innerHTML;
}

// Click on close button to delete a list item
function addfun() {
  var buttons = document.getElementsByClassName("Y");
  var i;
  for (i = 0; i < buttons.length; i++) {
    buttons[i].onclick = function() {
      var box = this.parentElement;
      box.classList.toggle("yes", true);
      box.classList.toggle("no", false);
      updatescore();
    }
  }
  var buttons = document.getElementsByClassName("N");
  var i;
  for (i = 0; i < buttons.length; i++) {
    buttons[i].onclick = function() {
      var box = this.parentElement;
      box.classList.toggle("yes", false);
      box.classList.toggle("no", true);
      updatescore();
    }
  }
  var buttons = document.getElementsByClassName("C");
  var i;
  for (i = 0; i < buttons.length; i++) {
    buttons[i].onclick = function() {
      var box = this.parentElement;
      box.classList.toggle("yes", false);
      box.classList.toggle("no", false);
      updatescore();
    }
  }
  var buttons = document.getElementsByClassName("P");
  var i;
  for (i = 0; i < buttons.length; i++) {
    buttons[i].onclick = function() {
      var box = this.parentElement;
      playAudio(box.dataset.filename);
      var list = document.getElementsByTagName("LI");
      for (i = 0; i < list.length; i++) {
        list[i].classList.toggle("current", false);
      }
      box.classList.toggle("current", true);
      updatescore();
    }
  }
}

addfun()

// Add check mark when an item has been clicked
var list = document.querySelector('ul');
list.addEventListener('click', function(event) {
  if (event.target.tagName === 'LI') {
    var allthem = document.getElementsByClassName("current");
    for (i = 0; i < allthem.length; i++) {
      allthem[i].classList.toggle("current", force = false)
    }
    event.target.classList.toggle('current');
    updatescore();
  }
}, false);


document.addEventListener('keydown', function(event) {
  switch (event.key) {
    case "y":
    case "Y":
      yHandler();
      break;
    case "n":
    case "N":
      nHandler();
      break;
    case "c":
    case "C":
      cHandler();
      break;
    case "ArrowUp":
      upHandler();
      break;
    case "ArrowDown":
      downHandler();
      break;
    case "Enter":
    case "Space":
    case "p":
    case "P":
      enterHandler();
      break
  }
});

function enterHandler() {
  var cur = document.getElementsByClassName("current");
  playAudio(cur[0].dataset.filename);
}

function upHandler() {
  var list = document.getElementsByTagName("LI");
  var spot = 0;
  for (i = 0; i < list.length; i++) {
    if (list[i].classList.contains("current")) {
      spot = i;
      list[i].classList.toggle("current");
    }
  }
  spot = (spot + list.length - 1) % list.length;
  list[spot].classList.toggle("current");
}


function downHandler() {
  var list = document.getElementsByTagName("LI");
  var spot = 0;
  for (i = 0; i < list.length; i++) {
    if (list[i].classList.contains("current")) {
      spot = i;
      list[i].classList.toggle("current");
    }
  }
  spot = (spot + list.length + 1) % list.length;
  list[spot].classList.toggle("current");
}

function yHandler() {
  var list = document.getElementsByTagName("LI");
  for (i = 0; i < list.length; i++) {
    if (list[i].classList.contains("current")) {
      list[i].classList.toggle("yes", force = true);
      list[i].classList.toggle("no", force = false);
    }
  }
  downHandler();
  updatescore();
}

function nHandler() {
  var list = document.getElementsByTagName("LI");
  for (i = 0; i < list.length; i++) {
    if (list[i].classList.contains("current")) {
      list[i].classList.toggle("yes", force = false);
      list[i].classList.toggle("no", force = true);
    }
  }
  downHandler();
  updatescore();
}

function cHandler() {
  var list = document.getElementsByTagName("LI");
  for (i = 0; i < list.length; i++) {
    if (list[i].classList.contains("current")) {
      list[i].classList.toggle("yes", force = false);
      list[i].classList.toggle("no", force = false);
    }
  }
  updatescore();
}

function updatescore() {
  var i = 0;
  var tot = 0;
  var totw = 0;
  var list = document.getElementsByTagName("LI");
  for (i = 0; i < list.length; i++) {
    if (list[i].classList.contains("yes")) {
      tot = tot + 1;
    }
    if (list[i].classList.contains("no")) {
      totw = totw + 1;
    }
  }
  var sb = document.getElementsByClassName("numcorrect");
  sb[0].innerHTML = tot;
  var sb = document.getElementsByClassName("numwrong");
  sb[0].innerHTML = totw;
}

/*
function newItem() {
  var li = document.createElement("li");
  var userInput = document.getElementById("newItem").value;
  var text = document.createTextNode(userInput);
    .appendChild(text);
     (userInput === '') {
    alert("You cannot submit a blank item!");
    else {
    document.getElementById("list1").appendChild(li);

  document.getElementById("newItem").value = "";

  createX(li);
  deleteItem();

*/
"""

with open(name+"/script.js","w") as f:
    f.write(s3)

