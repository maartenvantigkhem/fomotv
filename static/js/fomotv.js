/* Click Ripple effect*/
$(function() {
	var ink, d, x, y;
	$(".ripplelink").click(function(e) {
		if ($(this).find(".ink").length === 0) {
			$(this).prepend("<span class='ink'></span>");
		}

		ink = $(this).find(".ink");
		ink.removeClass("animate");

		if (!ink.height() && !ink.width()) {
			d = Math.max($(this).outerWidth(), $(this).outerHeight());
			ink.css({
				height: d,
				width: d
			});
		}

		x = e.pageX - $(this).offset().left - ink.width() / 2;
		y = e.pageY - $(this).offset().top - ink.height() / 2;

		ink.css({
			top: y + 'px',
			left: x + 'px'
		}).addClass("animate");
	});
});

/* Scroll to top*/
$(window).scroll(function() {
	if ($(document).scrollTop() < 100) {
		$(".top-site").fadeOut('slow');
	} else {

		$(".top-site").fadeIn('slow');

	}
});

$(".top-site i").on('click', function() {
	$("html, body").animate({
		scrollTop: 0
	}, 1000);
});

/* Klick after effect*/ (function() {

	// http://stackoverflow.com/a/11381730/989439
	function mobilecheck() {
		var check = false;
		(function(a) {
			if (/(android|ipad|playbook|silk|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino/i.test(a) || /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0, 4))) check = true
		})(navigator.userAgent || navigator.vendor || window.opera);
		return check;
	}

	var support = {
		animations: Modernizr.cssanimations
	},
		animEndEventNames = {
			'WebkitAnimation': 'webkitAnimationEnd',
			'OAnimation': 'oAnimationEnd',
			'msAnimation': 'MSAnimationEnd',
			'animation': 'animationend'
		},
		animEndEventName = animEndEventNames[Modernizr.prefixed('animation')],
		onEndAnimation = function(el, callback) {
			var onEndCallbackFn = function(ev) {
				if (support.animations) {
					if (ev.target != this) return;
					this.removeEventListener(animEndEventName, onEndCallbackFn);
				}
				if (callback && typeof callback === 'function') {
					callback.call();
				}
			};
			if (support.animations) {
				el.addEventListener(animEndEventName, onEndCallbackFn);
			} else {
				onEndCallbackFn();
			}
		},
		eventtype = mobilecheck() ? 'touchstart' : 'click';

	[].slice.call(document.querySelectorAll('.cbutton')).forEach(function(el) {
		el.addEventListener(eventtype, function(ev) {
			classie.add(el, 'cbutton--click');
			onEndAnimation(classie.has(el, 'cbutton--complex') ? el.querySelector('.cbutton__helper') : el, function() {
				classie.remove(el, 'cbutton--click');
			});
		});
	});

})();
/* Navbar shrink*/
$(window).scroll(function() {
	if ($(document).scrollTop() > 50) {
		$('nav').addClass('shrink-nav');
	} else {
		$('nav').removeClass('shrink-nav');
	}
});

/*floating labels form*/
$(function() {
	$("body").on("input propertychange", ".floating-label-form-group", function(e) {
		$(this).toggleClass("floating-label-form-group-with-value", !! $(e.target).val());
	}).on("focus", ".floating-label-form-group", function() {
		$(this).addClass("floating-label-form-group-with-focus");
	}).on("blur", ".floating-label-form-group", function() {
		$(this).removeClass("floating-label-form-group-with-focus");
	});
});
/*select skin underline*/

/***** Resize Image *****/
var resizeableImage = function(image_target) {
	// Some variable and settings
	var $container,
		orig_src = new Image(),
		image_target = $(image_target).get(0),
		event_state = {},
		constrain = false,
		min_width = 60, // Change as required
		min_height = 60,
		max_width = 1200, // Change as required
		max_height = 900,
		resize_canvas = document.createElement('canvas');

	init = function() {

		// When resizing, we will always use this copy of the original as the base
		//orig_src.src=image_target.src;

		// Wrap the image with the container and add resize handles
		$(image_target).wrap('<div class="resize-container"></div>')
			.before('<span class="resize-handle resize-handle-nw"></span>')
			.before('<span class="resize-handle resize-handle-ne"></span>')
			.after('<span class="resize-handle resize-handle-se"></span>')
			.after('<span class="resize-handle resize-handle-sw"></span>');

		// Assign the container to a variable
		$container = $(image_target).parent('.resize-container');

		// Add events
		$container.on('mousedown touchstart', '.resize-handle', startResize);
		$container.on('mousedown touchstart', 'img', startMoving);
		$('.js-crop').on('click', crop);
	};

	startResize = function(e) {
		e.preventDefault();
		e.stopPropagation();
		saveEventState(e);
		$(document).on('mousemove touchmove', resizing);
		$(document).on('mouseup touchend', endResize);
	};

	endResize = function(e) {
		e.preventDefault();
		$(document).off('mouseup touchend', endResize);
		$(document).off('mousemove touchmove', resizing);
	};

	saveEventState = function(e) {
		// Save the initial event details and container state
		event_state.container_width = $container.width();
		event_state.container_height = $container.height();
		event_state.container_left = $container.offset().left;
		event_state.container_top = $container.offset().top;
		event_state.mouse_x = (e.clientX || e.pageX || e.originalEvent.touches[0].clientX) + $(window).scrollLeft();
		event_state.mouse_y = (e.clientY || e.pageY || e.originalEvent.touches[0].clientY) + $(window).scrollTop();

		// This is a fix for mobile safari
		// For some reason it does not allow a direct copy of the touches property
		if (typeof e.originalEvent.touches !== 'undefined') {
			event_state.touches = [];
			$.each(e.originalEvent.touches, function(i, ob) {
				event_state.touches[i] = {};
				event_state.touches[i].clientX = 0 + ob.clientX;
				event_state.touches[i].clientY = 0 + ob.clientY;
			});
		}
		event_state.evnt = e;
	};

	resizing = function(e) {
		var mouse = {}, width, height, left, top, offset = $container.offset();
		mouse.x = (e.clientX || e.pageX || e.originalEvent.touches[0].clientX) + $(window).scrollLeft();
		mouse.y = (e.clientY || e.pageY || e.originalEvent.touches[0].clientY) + $(window).scrollTop();

		// Position image differently depending on the corner dragged and constraints
		if ($(event_state.evnt.target).hasClass('resize-handle-se')) {
			width = mouse.x - event_state.container_left;
			height = mouse.y - event_state.container_top;
			left = event_state.container_left;
			top = event_state.container_top;
		} else if ($(event_state.evnt.target).hasClass('resize-handle-sw')) {
			width = event_state.container_width - (mouse.x - event_state.container_left);
			height = mouse.y - event_state.container_top;
			left = mouse.x;
			top = event_state.container_top;
		} else if ($(event_state.evnt.target).hasClass('resize-handle-nw')) {
			width = event_state.container_width - (mouse.x - event_state.container_left);
			height = event_state.container_height - (mouse.y - event_state.container_top);
			left = mouse.x;
			top = mouse.y;
			if (constrain || e.shiftKey) {
				top = mouse.y - ((width / orig_src.width * orig_src.height) - height);
			}
		} else if ($(event_state.evnt.target).hasClass('resize-handle-ne')) {
			width = mouse.x - event_state.container_left;
			height = event_state.container_height - (mouse.y - event_state.container_top);
			left = event_state.container_left;
			top = mouse.y;
			if (constrain || e.shiftKey) {
				top = mouse.y - ((width / orig_src.width * orig_src.height) - height);
			}
		}

		// Optionally maintain aspect ratio
		if (constrain || e.shiftKey) {
			height = width / orig_src.width * orig_src.height;
		}

		if (width > min_width && height > min_height && width < max_width && height < max_height) {
			// To improve performance you might limit how often resizeImage() is called
			resizeImage(width, height);
			// Without this Firefox will not re-calculate the the image dimensions until drag end
			$container.offset({
				'left': left,
				'top': top
			});
		}
	}

	resizeImage = function(width, height) {
		resize_canvas.width = width;
		resize_canvas.height = height;
		resize_canvas.getContext('2d').drawImage(orig_src, 0, 0, width, height);
		$(image_target).attr('src', resize_canvas.toDataURL("image/png"));
	};

	startMoving = function(e) {
		e.preventDefault();
		e.stopPropagation();
		saveEventState(e);
		$(document).on('mousemove touchmove', moving);
		$(document).on('mouseup touchend', endMoving);
	};

	endMoving = function(e) {
		e.preventDefault();
		$(document).off('mouseup touchend', endMoving);
		$(document).off('mousemove touchmove', moving);
	};

	moving = function(e) {
		var mouse = {}, touches;
		e.preventDefault();
		e.stopPropagation();

		touches = e.originalEvent.touches;

		mouse.x = (e.clientX || e.pageX || touches[0].clientX) + $(window).scrollLeft();
		mouse.y = (e.clientY || e.pageY || touches[0].clientY) + $(window).scrollTop();
		$container.offset({
			'left': mouse.x - (event_state.mouse_x - event_state.container_left),
			'top': mouse.y - (event_state.mouse_y - event_state.container_top)
		});
		// Watch for pinch zoom gesture while moving
		if (event_state.touches && event_state.touches.length > 1 && touches.length > 1) {
			var width = event_state.container_width,
				height = event_state.container_height;
			var a = event_state.touches[0].clientX - event_state.touches[1].clientX;
			a = a * a;
			var b = event_state.touches[0].clientY - event_state.touches[1].clientY;
			b = b * b;
			var dist1 = Math.sqrt(a + b);

			a = e.originalEvent.touches[0].clientX - touches[1].clientX;
			a = a * a;
			b = e.originalEvent.touches[0].clientY - touches[1].clientY;
			b = b * b;
			var dist2 = Math.sqrt(a + b);

			var ratio = dist2 / dist1;

			width = width * ratio;
			height = height * ratio;
			// To improve performance you might limit how often resizeImage() is called
			resizeImage(width, height);
		}
	};

	crop = function() {
		//Find the part of the image that is inside the crop box
		var crop_canvas,
			left = $('.overlay').offset().left - $container.offset().left,
			top = $('.overlay').offset().top - $container.offset().top,
			width = $('.overlay').width(),
			height = $('.overlay').height();

		crop_canvas = document.createElement('canvas');
		crop_canvas.width = width;
		crop_canvas.height = height;

		crop_canvas.getContext('2d').drawImage(image_target, left, top, width, height, 0, 0, width, height);
		window.open(crop_canvas.toDataURL("image/png"));
	}

	init();
};

// Kick everything off with the target image
resizeableImage($('.resize-image'));


/** Isotope **/

/** Sidebars **/
$(document).ready(function() {
	$('#right-menu').sidr({
		name: 'sidr-right',
		side: 'right'
	});
});
$(document).ready(function() {
	$('#left-menu').sidr({
		name: 'sidr-left',
		side: 'left'
	});
});

$(document).ready(function() {
	$('label.tree-toggler').click(function() {
		$(this).parent().children('ul.tree').toggle(300);
	});
});