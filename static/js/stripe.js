$(function() {
    $("#payment-form").submit(function() {
      var form = this;
      var card = {
        number:   $("#id_credit_card_number").val(),
        expMonth: $("#id_expiry_month").val(),
        expYear:  $("#id_expiry_year").val(),
        cvc:      $("#id_cvv").val()
      };


    Stripe.createToken(card, function(status, response) {
        if (status === 200) {
          $("#credit-card-errors").hide();
          $("#id_stripe_id").val(response.id);
          
          // Prevent the Credit Card Details from being submitted to our server.
          $("#id_credit_card_number").removeAttr('name');
          $("#id_cvv").removeAttr('name');
          $("#id_cvv").removeAttr('name');
          $("#id_expiry_month").removeAttr('name');
          $("#id_expiry_year").removeAttr('name');

          form.submit();
        } else {
          $("#stripe-error-message").text(response.error.message);
          $("#credit-card-errors").show();
          $("#validate_card_btn").attr("disabled", false);
        }
    });
    return false;
  });
});



setTimeout(function() {
    $('input').addClass('animated tada');
}, 3000);

setTimeout(function() {
    $('.form').addClass('animated bounce');
}, 7000);

var config = {
      '.chzn-select'           : {},
      '.chzn-select-deselect'  : {allow_single_deselect:true},
      '.chzn-select-no-single' : {disable_search_threshold:10},
      '.chzn-select-no-results': {no_results_text:'Oops, nothing found!'},
      '.chzn-select-width'     : {width:"95%"}
    }
    for (var selector in config) {
      $(selector).chosen(config[selector]);
    }

$('body').on('change', '#model', function() {
        $('#trim_chzn').css('display', 'inline-block').addClass("chzn-container-active chzn-with-drop");
  $('#model_chzn, #make_chzn').width("auto").addClass('square');
  
  setTimeout(function() {
    $('#trim_chzn input').focus();
}, 200);
    });

$('body').on('change', '#year', function() {
       $('#make_chzn').addClass("chzn-container-active chzn-with-drop");
  
  setTimeout(function() {
    $('#make_chzn input').focus();
}, 200);

});

$('body').on('change', '#make', function() {
       $('#model_chzn').addClass("chzn-container-active chzn-with-drop");
  
setTimeout(function() {
    $('#model_chzn input').focus();
}, 200);
  
    });