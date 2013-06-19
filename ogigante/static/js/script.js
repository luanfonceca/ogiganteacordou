var cur = $('.posts div:first-child');
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