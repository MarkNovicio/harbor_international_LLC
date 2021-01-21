/*const signUpButton = document.getElementsByClassName('signUp');
console.log(signUpButton);
const signInButton = document.getElementById('signIn');
const container = document.getElementsByClassName('container');
console.log(container)

function addClass(name){
	console.log(name)
}
signUpButton.addEventListener("click", addClass("right-panel-active"));

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});
*/

$(document).ready(function() {
	$('.signUp').click(function(){
		$('#container').addClass("right-panel-active")
	})
	$('.signIn').click(function(){
		$('#container').removeClass("right-panel-active")
	})
})
