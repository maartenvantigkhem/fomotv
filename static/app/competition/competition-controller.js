/**
 * Compatition page controller
 */
(function () {
    'use strict';

    angular
        .module('mainApp')
        .controller('CompetitionController', CompetitionController);

    CompetitionController.$inject = ['$scope', '$window', '$routeParams', '$timeout', '$location', 'CompetitionService',
        'ezfb', 'Auth', 'PrizeService'];

    function CompetitionController($scope, $window, $routeParams, $timeout, $location, CompetitionService, ezfb, Auth, PrizeService) {
        //active competition
        $scope.competition = CompetitionService.getCompetition();

        //get list of available competitions
        $scope.competitionList = [];
        CompetitionService.getActiveList().then(function (data) {
            $scope.competitionList = data;
        });

        //flag for header blocks
        $scope.competitionPageFlag = true;

        //prizes
        $scope.prizes = [];
        $scope.bestPhotoPrizes = [];
        $scope.randomVotePrizes = [];

        //selected prize in product detail block
        $scope.selectedPrize = null;

        //share options
        $scope.currentUrl = $location.absUrl();
        $scope.shareName = "Prized.tv";
        $scope.shareText = "Sharing and voting for this might win me a prize this week, you can win one too if you click here.Prized.tv";
        $scope.shareCaption = "prized.tv";

        //intro for new users
        $scope.introViewed = false;

        //competition photos
        $scope.photos = [];
        //current active photo
        $scope.currentIndex = 0;

        $scope.vote = function (photoId, voteFlag) {
            //console.log(photoId, voteFlag);
            if(!Auth.isAuth()) {
                Auth.showLoginPopup();
            }
            else {
                CompetitionService.vote(photoId, $scope.competition.id, voteFlag ? 1 : 0).then(
                    function() {
                        $scope.currentIndex++;
                        if($scope.photos.length - $scope.currentIndex < 5) {
                            if (typeof $routeParams.photo_id != 'undefined') {
                                //window.location = "/#!/competition/" + $scope.competition.id;
                            }
                            else {
                                //$window.location.reload();
                            }
                        }
                        console.log($scope.photos.length - $scope.currentIndex);
                    }

                );

            }
        };

        $scope.sendAbuse = function (type) {
            var photoId = $scope.photos[$scope.currentIndex].id;
            $('#abuse-opt').modal('hide');
            CompetitionService.abuse(photoId, type).then(function () {
                $timeout(function () {
                    $scope.$parent.showInfoMessage("Message sended");
                }, 0);
            });
        };

        $scope.pinShare = function() {
            var host = "http://www.prized.tv/";
            var url = host + "/competition/" + $scope.competition.id;
            var media = $scope.photos[$scope.currentIndex].image;
            var desc = $scope.shareText;
            window.open("//www.pinterest.com/pin/create/button/" +
                "?url=" + url +
                "&media=" + media +
                "&description=" + desc, "_blank");
        };

        $scope.fbShare = function () {
            ezfb.ui(
                {
                    method: 'feed',
                    name: $scope.shareName,
                    picture: $scope.photos[$scope.currentIndex].image,
                    link: $scope.currentUrl,
                    description: $scope.shareText,
                    caption: $scope.shareCaption
                },
                function (res) {
                    if (res !== null) {
                        var photoId = $scope.photos[$scope.currentIndex].id;
                        CompetitionService.share(photoId, $scope.competition.id);
                    }
                }
            );
        };

        $scope.removeIntro = function() {
            createCookie("introViewed", true, 365);
            $scope.introViewed = true;
        };

        $scope.drag_flag = false;

        $scope.startDrag = function() {
            $scope.drag_flag = true;
            console.log('drag start');
        };

        $scope.showGifPopup = function() {
            // show tip on user click on photo
            if($scope.drag_flag == false) {
                $('#click-tip-popup').modal("show");
            }
        };

        $scope.lookAtPhotoAgain = function() {
            CompetitionService.cleanViewHistory($scope.competition.id).then(function() {
                $window.location.reload();
            });
        };

        function init() {
            //if competition not found
            if ($scope.competition === null) {
                $location.url("/");
            }

            if ($scope.competition.active_flag != true) {
                $location.url("/");
            }

            //alert ($scope.competition.end_date)
            //remove intro in viewed by user
            if(readCookie("introViewed") != null) {
                 $scope.introViewed = true;
            }

            PrizeService.getCurrentWeekList().then(function(data) {
                $scope.prizes = data;

                if (typeof $routeParams.prize_id != 'undefined') {
                    var result = $.grep($scope.prizes, function (e) {
                        return e.id == $routeParams.prize_id;
                    });

                    if (result.length == 1) {
                        $scope.selectedPrize =  result[0];
                    }
                    else {
                        $location.url("/");
                    }

                    $timeout(function () {
                        $("html, body").animate({
                            scrollTop: $(".product-details").offset().top
                        }, 1000);
                    }, 10);
                }
                else {
                    $scope.selectedPrize = CompetitionService.getFirstPrize();
                }

                //get best photo/random vote prize lists
                $scope.randomVotePrizes = $.grep($scope.prizes, function(v) {
                    return v.prize_type === "rv";
                });

                $scope.bestPhotoPrizes = $.grep($scope.prizes, function(v) {
                    return v.prize_type === "bp";
                });
            });

            var photoId = typeof $routeParams.photo_id != 'undefined'?$routeParams.photo_id:0;
            CompetitionService.loadPhotos($scope.competition.id, photoId).then(function () {
                $scope.photos = CompetitionService.getPhotos();
            });

            window.twttr.ready(function(twttr) {
                // Now bind our custom intent events
                window.twttr.events.bind('tweet', function(e) {
                    var photoId = $scope.photos[$scope.currentIndex].id;
                    CompetitionService.share(photoId, $scope.competition.id);
                });
            });

            $timeout(function () {

                $('.dress-cover-box .gallery-main').flickity();
                // 2nd gallery, navigation
                $('.dress-cover-box .gallery-nav').flickity({
                    asNavFor: '.gallery-main',
                    contain: true,
                    pageDots: false
                });

                $(".compet-carousel li, .pr-carousel li, .play-stop-rocket ul li").on('click', function() {
                    $("html, body").animate({
                        scrollTop: $('#product_view').offset().top
                    }, 1000);
                });

                $(".term").on('click', function() {
                    $("html, body").animate({
                        scrollTop: $('#footer').offset().top
                    }, 1000);
                });
                $(window).scroll(function() {
                    if ($(document).scrollTop() < 100) {
                        $(".top-site").fadeOut('slow');
                    } else {

                        $(".top-site").fadeIn('slow');

                    }
                });

                $(".top-site i").on('click', function () {
                    $("html, body").animate({
                        scrollTop: 0
                    }, 1000);
                });

                $('.captions').flowtype();

                /* scroll on click end */
                Main_Menu();

                $('.nav-mob').click(function (e) {
                    $('.nav-menu').slideToggle('slow');
                });

                album_menu();
                $('.btn-alb-mob-filt').click(function (e) {
                    $('body').toggleClass('mob-pdl200');
                    $('.alb-list-mob').toggleClass('active');
                    $('.mob-pdl200').css('width', Win_w);
                    e.stopPropagation();
                });

                //Album_select();

                //Album_Image_selct();

                //Dropdown1();
                //Color_Choose();
                //Size_Choose();

                //Detail_Accordion();

            }, 1000);
        }

        init();
    }

    angular.module('mainApp')
        .directive('voteCarousel', function () {

            var elastic = null;

            return function (scope, element, attrs) {
                if (scope.$last) {
                    new ElastiStack(document.getElementById('elasticstack'));
                }
        };
    })

})();
