$(".flashes .dismiss").click(e => {
  $(".flashes").remove();
})

const slideout = new Slideout({
  'panel': document.getElementById('panel'),
  'menu': document.getElementById('m-menu'),
  'padding': 256,
  'tolerance': 70,
  'side': 'right'
});

$(".toggle-button").click(e=> {
  slideout.toggle();
})