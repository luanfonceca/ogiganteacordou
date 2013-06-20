var cur = $('.posts div.post:first-child');
cur.addClass('focus');

$('html, body').on('keyup', function(e) {
    e.stopPropagation();
    var code = (e.keyCode ? e.keyCode : e.which);
    if (code == 74 || code == 40) {
        cur.removeClass('focus');
        if ( cur.next().length > 0 ) cur = cur.next();
        cur.addClass('focus');
        $('html, body').scrollTop(cur.offset().top-100);
    } else if (code == 75 || code == 38 ) {
        cur.removeClass('focus');
        if ( cur.prev().length > 0 ) cur = cur.prev();
        cur.addClass('focus');
        $('html, body').scrollTop(cur.offset().top-100);
    }
});

$("#form_entry").validate({
    rules:{
        title: {
            required: true
        },
        text: {
            required: true
        },
        recaptcha_response_field: {
            required: true
        },
    },
    errorClass: "help-inline",
    errorElement: "span",
    highlight: function(element, errorClass, validClass) {
        $(element).parents('.control-group').addClass('error');
    },
    unhighlight: function(element, errorClass, validClass) {
        $(element).parents('.control-group').removeClass('error');
    }
});

// NOTE: Force close of the messages
$('.alert button.close').click(function() {
    $(this).parent().remove();
});
