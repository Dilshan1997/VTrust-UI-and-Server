$(function () {
    $('#ballot_form').parsley().on('field:validated', function() {
      var ok = $('.parsley-error').length === 0;
      $('.bs-callout-info').toggleClass('hidden', !ok);
      $('.bs-callout-warning').toggleClass('hidden', ok);
    })
    .on('form:submit', function() {
      return true; 
    });
  });

  // $(function () {
  //   $('#register_form').parsley().on('field:validated', function() {
  //     var ok = $('.parsley-error').length === 0;
  //     $('.bs-callout-info').toggleClass('hidden', !ok);
  //     $('.bs-callout-warning').toggleClass('hidden', ok);
  //   })
  //   .on('form:submit', function() {
  //     return true; 
  //   });
  // });
