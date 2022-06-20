let navBrand = document.querySelector(".navbar-brand");

navBrand.addEventListener("click", ()=>{
    location.reload()
})

/* particlesJS.load(@dom-id, @path-json, @callback (optional)); */
particlesJS.load('particles-js', 'static/particlesjs-config.json', function() {
    console.log('callback - particles.js config loaded');
  });