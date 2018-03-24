
 
window.onload =function(){
	 var text= document.getElementById("text-be");
	 var show= document.getElementById("text-af");
	 var i=0;
	 timer=setInterval(function(){
		 show.innerHTML=text.innerHTML.substring(0,i);
		 i++;
		 if(show.innerHTML==text.innerHTML){
			 clearInterval(timer);
		 }
	 } ,140);
 }

$(document).ready(function(){
  $("button").click(function(){
    $("left").fadeIn(slow);
   
  });
});