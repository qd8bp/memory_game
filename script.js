function playAudio(url) {
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
