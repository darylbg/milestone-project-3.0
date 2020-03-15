//sidenav
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.sidenav');
  var instances = M.Sidenav.init(elems);
});

document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.datepicker');
  var instances = M.Datepicker.init(elems);
});


//Get the button:
mybutton = document.getElementById("myBtn");


// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {
  scrollFunction()
};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

//selector forms

document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('select');
  var instances = M.FormSelect.init(elems);
});

// Glide.js carousel

const options = {
  type: 'slider',
  perView: 5.2,
  gap: 50,
  breakpoints: {
    440: {
      perView: 1.2,
      gap: 20
    },
    900: {
      perView: 2.2,
      gap: 20
    },
    1100: {
      perView: 3.2,
      gap: 30
    },
    1400: {
      perView: 4.2,
      gap: 30
    },
    1600: {
      perView: 4.2,
      gap: 40
    }
  }
}
new Glide('.glide', options).mount()
