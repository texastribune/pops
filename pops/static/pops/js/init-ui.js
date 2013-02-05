$(function(){
	$('select').chosen();
	$('.vDateField').datepicker({dateFormat: 'yy-mm-dd'});

  $('textarea').each(function(){
    // plugin does not work on collections
    $(this).wysihtml5();
  });
});

