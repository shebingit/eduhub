window.addEventListener("load", function()
{
  setTimeout(
    function open(event)
    {
      document.querySelector(".popup_box_offer").style.display="block";
    },2000
  )
});



document.querySelector("#close_popup").addEventListener("click", function()
{
document.querySelector(".popup_box_offer").style.display="none";
});














