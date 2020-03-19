//sidenav
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.sidenav');
  var instances = M.Sidenav.init(elems);
});

//datepicker
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.datepicker');
  var instances = M.Datepicker.init(elems);
});


//scroll to top button
mybutton = document.getElementById("myBtn");

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


function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

//search autocomplete
$(document).ready(function(){
    $('input.autocomplete').autocomplete({
      data: {
        "Alabama": null,
        "Alaska": null,
        "Arizona": null,
        "Arkansas": null,
        "California": null,
        "Colorado": null,
        "Connecticut": null,
        "Delaware": null,
        "Florida": null,
        "Georgia": null,
        "Hawaii": null,
        "Idaho": null,
        "Illanois": null,
        "Indiana": null,
        "Iowa": null,
        "Kansas": null,
        "Kentucky": null,
        "Louisiana": null,
        "Maine": null,
        "Maryland": null,
        "Massachusetts": null,
        "Michigan": null,
        "Minnesota": null,
        "Mississippi": null,
        "Missouri": null,
        "Montana": null,
        "Nebraska": null,
        "Nevada": null,
        "New Hampshire": null,
        "New Jersey": null,
        "New Mexico": null,
        "New York": null,
        "North Carolina": null,
        "Noth Dakota": null,
        "Ohio": null,
        "Oklahoma": null,
        "Oregon": null,
        "Pennsylvania": null,
        "Rhode Island": null,
        "South Carolina": null,
        "South Dakota": null,
        "Tennessee": null,
        "Texas": null,
        "Utah": null,
        "Vermont": null,
        "Virginia": null,
        "Washington": null,
        "West Virginia": null,
        "Wisconsin": null,
        "Wyoming": null
      },
    });
  });

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
