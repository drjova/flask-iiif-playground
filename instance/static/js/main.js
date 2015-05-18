$(document).ready(function(){
  var $main = $('#main');
  var prefix = $main.data('base');
  var $imageWrapper = $('#image-1-wrapper');
  var $imageForm = $('#image-1-form');
  var loader1 = $('.loader-1');
  var reset = ['full', 'full', '0', 'default', 'png'];
  $('.url-prefix').text(prefix);
  var counter = 1;
  // Init
  function init(){
    update_image();
    $main.addClass('form-inline');
    $('input').addClass('form-control');
  }
  function update_image(){
    loader1.show();
    if (counter > 1){
      $('.reset-button').css('visibility', 'visible');
    }else{
      $('.reset-button').css('visibility', 'hidden');
    }
    var suffix;
    // Kill image from the dom
    var data = $imageForm.serializeArray();
    suffix = data[0].value+'/'+data[1].value+'/'+data[2].value+ '/'+data[3].value +'.'+ data[4].value;
    var src = prefix+'/'+suffix;
    $('#image-1').hide();
    $('<img/>')
     .load(function(){
      add_image(src);
      loader1.hide();
     })
     .error(function(error, errorText){
        loader1.hide();
        console.log('error', errorText);
        alert('Error');
      })
     .attr('src', src);
    counter++;
  }
  function add_image(src){
    $('#image-1').attr('src', src);
    $('#image-1').show();
  }
  function reset_default(){
    location.reload();
  }
  // Add bindings
  init();
  $imageForm.on('change', update_image);
  $('.reset-button').on('click', reset_default);
  $('[data-toggle="tooltip"]').tooltip()
  $(window).on('resize', resize);
  function resize(){
    $('.image-1-wrapper').css('height', $(window).height() - 110);
  }
  resize();
})
