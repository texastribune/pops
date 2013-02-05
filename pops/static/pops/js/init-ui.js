$(function(){
	$('select').chosen();
	$('.vDateField').datepicker({dateFormat: 'yy-mm-dd'});

  $('textarea').each(function(){
    // plugin does not work on collections
    var static_url = '/common/';
    var options = {
      "font-styles": false,
      "html": true,
      "image": false,
      "stylesheets": [
        static_url + "css/reset.css",
        static_url + "css/texastribune.css",
        static_url + "css/editorial.css"
      ]
    };
    $(this).wysihtml5(options);
  });
});

