//global variables
/*
let parentCommentContainer = document.getElementsByClassName(
  "testimonial-body"
);


$("#enter-container").hover(
  function () {
    var door = document.getElementById("enter-door");
    $(door).show();
  },
  function () {
    var door = document.getElementById("enter-door");
    $(door).hide();
  }
);
*/
let imageArray = [
  {
    image: "assets/images/mountains.jpg",
    description: "Health stuff",
  },
  {
    image: "assets/images/swaziland_kids_health_center.jpg",
    description: "mountains",
  },
];
let accomplishmentsParent = [
  {
    header: "Parent",
    image: "",
    name: "John Doe",
    location: "Washington DC",
    message:
      "Ifadfad adfdf fdsafd af fadfsa fsdfasf afadfa afasdfa fadf jkjkjlkajfda fafads fad fasd fadaf",
  },

  {
    header: "Parent",
    image: "",
    name: "John Doe",
    location: "Berwyn Heights, MD",
    message:
      "afasddfadfdf fdsafd af fadfsa fsdfasf afadfa afasdfa fadf jkjkjlkajfda fafads fad fasd fadaf",
  },
  {
    header: "Parent",
    image: "",
    name: "John Doe",
    location: "College Park, MD",
    message:
      "O ilke apples fdsafd af fadfsa fsdfasf afadfa afasdfa fadf jkjkjlkajfda fafads fad fasd fadaf",
  },
];
/*
function establishComments() {
  let currentComment = 0;
  setParentTestimonials();
}
*/
/*
let parentCommentContainer = document.getElementById("testimonial-body");

function loopThroughContent() {
  let currentIndex = 0;
  setTestimonialHeader(currentIndex);
  setTestimonialName(currentIndex);
  setTestimonialLocation(currentIndex);
  setTestimonialMessage(currentIndex);
  setImageContent(currentIndex);

  //next button clicked
  $(".next-page").on("click", function (event) {
    event.preventDefault();
    console.log("works");

    currentIndex++;
    console.log(currentIndex);

    if (
      currentIndex === accomplishmentsParent.length ||
      currentIndex === imageArray.length
    ) {
      currentIndex = 0;
    }
    setTestimonialHeader(currentIndex);
    setTestimonialName(currentIndex);
    setTestimonialLocation(currentIndex);
    setTestimonialMessage(currentIndex);
    setImageContent(currentIndex);
    //setImage(currentImage);
    console.log("works");
  });
*/
  $(".prev-page").click(function (event) {
    event.preventDefault();
    console.log("works");
    //event.preventDefault();
    currentIndex--;
    if (currentIndex < 0) {
      currentIndex = accomplishmentsParent.length - 1;
    }
    //setImage(currentImage);
    setTestimonialHeader(currentIndex);
    setTestimonialName(currentIndex);
    setTestimonialLocation(currentIndex);
    setTestimonialMessage(currentIndex);
    setImageContent(currentIndex);
  });


function setTestimonialName(idx) {
  let nameText = document.querySelector(".name-container");
  nameText.innerHTML = accomplishmentsParent[idx].name;
}

function setTestimonialLocation(idx) {
  let locationText = document.querySelector(".location-container");
  locationText.innerHTML = accomplishmentsParent[idx].location;
}

function setTestimonialMessage(idx) {
  let messageText = document.querySelector(".message-container");
  messageText.innerHTML = accomplishmentsParent[idx].message;
}

function setImageContent(idx) {
  let imageElement = document.querySelector(".photo-container");
  imageElement.style.backgroundImage = "url(" + imageArray[idx].image + ")";
  imageElement.style.backgroundSize = "100%";
  imageElement.style.backgroundRepeat = "fixed";
  $(".photo-content").text(`${imageArray[idx].description}`);
}
function windowSignIn() {
window.addEventListener('load', function() {
  /*If user login is Algebra display Algebra 
  related elements on the page */
  


  console.log('page is fully loaded');

})
};

function showContent(){
  window.addEventListener('click', function(event){
    
    if (event.target.classList.contains("plus-svg-image") || (event.target.classList.contains("topic-2"))) {
      listLength= document.querySelectorAll(".unit li")
    console.log(listLength)
      for(let i=0; i<listLength.length-2; i++){
      document.getElementsByClassName("topic-2")[i].style.display = "block"
      
    }
    console.log("worked")

    document.getElementsByClassName("plus-svg-image")[1].style.display = "none"
    document.getElementsByClassName("minus-svg-image")[1].style.display = "inline"
    }

  },
  false
  );
}
showContent()

function pageLoad() {
  window.onload
}

function hideContent(){
  window.addEventListener('click', function(event){
    
    if (event.target.classList.contains("minus-svg-image")) {
      listLength= document.querySelectorAll(".unit li")
    console.log(listLength)
      for(let i=0; i<listLength.length-2; i++){
      document.getElementsByClassName("topic-2")[i].style.display = "none"
      
    }
    console.log("worked")
    
    document.getElementsByClassName("minus-svg-image")[1].style.display = "none"
    document.getElementsByClassName("plus-svg-image")[1].style.display = "inline"
    }
  },
  false
  );
}
hideContent()

windowSignIn()
/*
function setParentTestimonials(idx) {
  //let commentArr = accomplishmentsParent[idx];
  //let commentContainer = parentCommentContainer; //target the element
  //let content = document.createTextNode("stuuf");
  console.log("works");
  console.log(parentCommentContainer);
  let existingText = parentCommentContainer.innerHTML;
  const createNameElement = document.createElement("p");
  createNameElement.id = parentCommentContainer.innerHTML =
    existingText + accomplishmentsParent[idx].name;
  const createLocationElement = document.createElement("p");
  createLocationElement.id = "comment-header";
  createLocationElement.textContent = accomplishmentsParent[idx].location;
  parentCommentContainer.append(createLocationElement);

  const createMessageElement = document.createElement("p");
  createMessageElement.id = "comment-body";
  createMessageElement.textContent = accomplishmentsParent[idx].message;
  parentCommentContainer.append(createMessageElement);
}
*/

//setParentTestimonials(0);
//setTestimonialHeader(0);
