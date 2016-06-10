/**
 * Questionnaire page controller
 */
(function () {
    'use strict';

    angular
        .module('mainApp')
        .controller('QuestionnaireController', QuestionnaireController);

    QuestionnaireController.$inject = ['$scope', '$window', '$routeParams', '$timeout', '$location', 'QuestionnaireService',
        'ezfb', 'Auth', 'ngCart'];

    function QuestionnaireController($scope, $window, $routeParams, $timeout, $location, QuestionnaireService, ezfb, Auth, ngCart) {
        //active questionnaire
        $scope.questionnaire = QuestionnaireService.getQuestionnaire();
        $scope.questions = [];
        $scope.finished = false;
        $scope.moreQuestionnaires = [];
        $scope.showQuestionnairePrizeSlide = false;
        $scope.winPrize = false;

        //flag for header blocks
        $scope.questionnairePageFlag = false;

        //prizes
        $scope.prizes = QuestionnaireService.getPrizes();
        $scope.bestPhotoPrizes = [];
        $scope.randomVotePrizes = [];

        //selected prize in product detail block
        $scope.selectedPrize = null;

        //share options
        $scope.currentUrl = $location.absUrl();
        $scope.shareName = "Prized.tv";
        $scope.shareText = "Prized.tv - Make your photos famous!";

        //intro for new users
        $scope.introViewed = true;

        //current active photo
        $scope.currentIndex = 0;

        $scope.vote = function (questionId, voteFlag) {
            if(!Auth.isAuth()) {
                Auth.showLoginPopup();
            }
            else {
                QuestionnaireService.save_answer(questionId, voteFlag ? 1 : 0).then(function(res) {
                    console.log(res);
                    if(res.data.finished == 1) {
                        //show results here
                        $scope.finished = true;
                        $scope.userResult = res.data.user_result;
                        $scope.results = res.data.results;
                        $scope.showQuestionnairePrizeSlide = true;
                        $scope.winPrize = res.data.win_prize;
                    }
                });
                $scope.currentIndex++;
                console.log($scope.questions.length - $scope.currentIndex);
            }
        };

        $scope.sendAbuse = function (type) {
            var photoId = $scope.photos[$scope.currentIndex].id;
            $('#abuse-opt').modal('hide');
            QuestionnaireService.abuse(photoId, type).then(function () {
                $timeout(function () {
                    $scope.$parent.showInfoMessage("Message sended");
                }, 0);
            });
        };

        $scope.fbShare = function () {
            ezfb.ui(
                {
                    method: 'feed',
                    name: $scope.shareName,
                    picture: $scope.photos[$scope.currentIndex].image,
                    link: $scope.currentUrl,
                    description: $scope.shareText,
                    caption: $scope.shareText
                },
                function (res) {
                    if (res !== null) {
                        var photoId = $scope.photos[$scope.currentIndex].id;
                        QuestionnaireService.share(photoId);
                    }
                }
            );
        };

        function init() {
            //if questionnaire not found
            if ($scope.questionnaire === null) {
                $location.url("/");
            }

            if ($scope.questionnaire.active_flag != true) {
                $location.url("/");
            }

            //remove intro in viewed by user
            if(readCookie("introViewed") != null) {
                 $scope.introViewed = true;
            }

            if (typeof $routeParams.prize_id != 'undefined') {
                $scope.selectedPrize = QuestionnaireService.getPrizeById($routeParams.prize_id);

                if ($scope.selectedPrize === null) {
                    $location.url("/"); //change to 404 not found page?
                }

                $timeout(function () {
                    $("html, body").animate({
                        scrollTop: $(".product-details").offset().top
                    }, 1000);
                }, 10);
            }
            else {
                $scope.selectedPrize = QuestionnaireService.getFirstPrize();
            }

            QuestionnaireService.getListForUser().then(function(res) {
                $scope.moreQuestionnaires = res;

            });

            QuestionnaireService.getResult($scope.questionnaire.id).then(function(res) {
                if (res.data.finished == 1) {
                    $scope.finished = true;
                    $scope.userResult = res.data.user_result;
                    $scope.results = res.data.results;
                }
                else {
                    $scope.questions = $scope.questionnaire.questions;
                }

                 $scope.$broadcast('dataloaded');
            });


            window.twttr.ready(function(twttr) {
                // Now bind our custom intent events
                window.twttr.events.bind('tweet', function(e) {
                    var photoId = $scope.photos[$scope.currentIndex].id;
                    QuestionnaireService.share(photoId);
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

                Album_select();

                Album_Image_selct();

                Dropdown1();
                Color_Choose();
                Size_Choose();

                Detail_Accordion();

            }, 1000);
        }

        init();
    }

    angular.module('mainApp')
        .directive('quizCarousel', ['$timeout', function ($timeout) {
            return {
                link: function ($scope, element, attrs) {
                    $scope.$on('dataloaded', function () {
                        $timeout(function () { // You might need this timeout to be sure its run after DOM render.
                             new ElastiStack(document.getElementById('elasticstack'));
                        }, 0, false);
                    })
                }
            };
        }])


})();
