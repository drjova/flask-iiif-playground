$(document).ready(function(){
  $(window).on('resize', init);
  function init(){
    $('#map').css('height', $(window).height() - 60);
    $('.main-nav > a').on('click', function(){
      window.stop();
    });
  }
  init();
});
