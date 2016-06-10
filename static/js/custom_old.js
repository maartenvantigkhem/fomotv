$(document).ready(function(e) {
	
	Main_Menu();
	
	$('.nav-mob').click(function(e) {
        $('.nav-menu').slideToggle('slow');
    });
	
	album_menu();
	$('.btn-alb-mob-filt').click(function(e) {
		$('body').toggleClass('mob-pdl200');
		$('.alb-list-mob').toggleClass('active');
		$('.mob-pdl200').css('width',Win_w);
		e.stopPropagation();
	});
	
	//Album_select();
	
	//Album_Image_selct();
	
	//Dropdown();
	//Color_Choose();
	//Size_Choose();
	
	//Detail_Accordion();
	
	// Carousel Start
/*

	$('.pr-carousel, .compet-carousel').bxSlider({
		minSlides: 1,
		maxSlides: 7,
		moveSlides: 1,
		slideWidth: 180,
		slideMargin: 10
	});
*/
	$('.contest-carousel').bxSlider({
		minSlides: 1,
		maxSlides: 3,
		moveSlides: 1,
		slideWidth: 400
	});
	
	$('.pro-slider').bxSlider({
	  pagerCustom: '#bx-pager'
	});
	
	// Album Scrollbar Start
/*
    (function($){
		$(window).load(function(){
			$("#alb-scrollber").mCustomScrollbar({
				axis:"y",
				scrollButtons:{enable:true},
				theme:"dark-3",
				//scrollbarPosition:"outside"
			});
		});
	})(jQuery);


	// Size Guide Popup Start
    $('#size-guide').popup({
        pagecontainer: '.container',
        transition: 'all 0.3s'
    });

	// Add to Bag Popup Start
	$('#add-to-bag-status').popup({
        pagecontainer: '.container',
        transition: 'all 0.3s'
    });
	$('#share-photo').popup({
        pagecontainer: '.container',
        transition: 'all 0.3s'
    });
	$('#share-photo1').popup({
        pagecontainer: '.container',
        transition: 'all 0.3s'
    });
	$('#share-photo2').popup({
        pagecontainer: '.container',
        transition: 'all 0.3s'
    });
	
*/
	/** slow scroll **/
	
	$('.play-stop-rocket ul li a[href^="#"], .play-stop-rocket ul li a[href^="#"]').click(function() {

			$('html,body').animate({ scrollTop: $(this.hash).offset().top}, 1000);
			
			return false;
			
			e.preventDefault();
			
			});
	/** slow scroll end **/		
	
});
$(window).resize(function(e) {
	Main_Menu();
	album_menu();
});

// Function Stop
function stopPropagation(e) {
    if(e.stopPropagation) {
        e.stopPropagation();
    } else {
        e.returnValue = false;
    }    
}
// Click Document close
$(document).click(function(e) {
	$('.dropdown-box').slideUp('slow');
	
	$('body').removeClass('mob-pdl200');
	$('.alb-list-mob').removeClass('active');
	$('body').css('width','');
}); 
// Main Menu Start
function Main_Menu(){
	$(window).scroll(function(e) {
		Win_scroll = $(window).scrollTop();
		if(Win_scroll>= 100){
			$('.btn-mob').css({
				color:'#46c4a8',
				'border-color': '#46c4a8',
			});
		}else{
			$('.nav-mob').css({
				color:'#fff',
				'border-color': '#fff',
			});
		}
	});
	Win_w = $(window).width();
	if(Win_w>=992){
		$('.nav-menu').css('display', 'block');
	}
	else{
		$('.nav-menu').css('display', 'none');
	}
}

// Album List Mobile Start
function album_menu(){
	Win_w = $(window).width();
	if(Win_w>=992){
		$('body').removeClass('mob-pdl200');
		$('.alb-list-mob').removeClass('active');
		$('body').css('width','');
	}
}

// Album List Start
function Album_select(){
	$('.alb-list li').click(function(e) {
		$(this).siblings().removeClass('selected');
        $(this).addClass('selected');
    });
}
// Album Image Selecttion Start
function Album_Image_selct(){
 	$('.alb-img-ful-box > .alb-img-box').click(function(){
  		if($('.alb-img-ful-box > .alb-img-box').filter('.selected').length < 3){
   			$(this).toggleClass('selected');
  		}
  		else{
   			$(this).removeClass('selected');
  		}
 	});
}

// Dropdown Start
function Dropdown(){
	$('.dropdown').click(function(e) {
		$(this).parent().siblings().children('.dropdown-box').slideUp('slow');
		$(this).siblings('.dropdown-box').slideToggle('slow');
		e.stopPropagation();
    });
}
// Product Color Choose Start
function Color_Choose(){
	$('.dress-drop-clr-list li').click(function(e) {
        Choose_Color = $(this).html();
		Color_Box = $('.dress-color-box').html(Choose_Color);
    });
}

// Product Size Choose Start
function Size_Choose(){
	$('.dress-drop-size-list li').click(function(e) {
        Choose_Size = $(this).find('.size-no').text();
		Size_Box = $('.dress-size-box p').text(Choose_Size);
    });
}
// Product Detail Accordion Start
function Detail_Accordion(){
	$('.dress-detail .dress-detail-heading').click(function(e) {
        $(this).find('.dress-detail-icon > i').toggleClass('fa-plus','fa-minus');
		//$(Find_icon).addClass('fa-plus');
		//Size_Box = $('.dress-size-box p').text(Choose_Size);
		$(this).parent().siblings().children('.dress-detail .dress-detail-cont').slideUp('slow');
		$(this).siblings('.dress-detail .dress-detail-cont').slideToggle('slow');
    });
}



