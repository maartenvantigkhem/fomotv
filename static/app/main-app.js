angular.module('mainApp', ['ngRoute', 'ngSanitize', 'ngCookies', 'ezfb', 'ngCart', 'ngImgCrop', 'myConfig', 'rzModule', 'selector'])
    .config(['ezfbProvider', '$httpProvider', '$logProvider', '$locationProvider', '$compileProvider', 'appConfig',
        function (ezfbProvider, $httpProvider, $logProvider, $locationProvider, $compileProvider, appConfig) {
            ezfbProvider.setInitParams({
                appId: appConfig.facebookAppId
            });
            $logProvider.debugEnabled(false);
            $compileProvider.debugInfoEnabled(true);

            $locationProvider.hashPrefix("!");

            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
            $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

        }])
    .run(['$rootScope', '$window', '$timeout', 'Auth', function ($rootScope, $window, $timeout, Auth) {

        wow = new WOW(
            {
                animateClass: 'animated',
                offset: 100
            }
        );
        wow.init();

        $rootScope.$on('$routeChangeSuccess', function (next, current) {
            //when the view changes sync wow
            $('.modal').modal('hide');

            Auth.checkTermsFlag();

            wow.sync();
            $window.scrollTo(0, 0);

            $(window).scroll(function () {
                if ($(document).scrollTop() < 100) {
                    $(".top-site").fadeOut('slow');
                }
                else {

                    $(".top-site").fadeIn('slow');
                }
            });

            $(".top-site i").on('click', function () {
                //alert("1");
                $("html, body").animate({
                    scrollTop: 0
                }, 1000);
            });

            $timeout(function() {
               $('#right-menu').sidr({
                      name: 'sidr-right',
                      side: 'right'
                    });
                   $('#left-menu').sidr({
                      name: 'sidr-left',
                      side: 'left'
                    });

                    $('label.tree-toggler').click(function () {
                        $(this).parent().children('ul.tree').toggle(300);
                    });
            }, 100);

        });
    }])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider
            .when('/home', {
                controller: 'IndexController',
                templateUrl: 'static/app/templates/index.html',
                resolve: {
                    competition: function (CompetitionService) {
                        return CompetitionService.getActive();
                    }
                }
            })
            .when('/', {
                controller: 'IndexController',
                templateUrl: 'static/app/templates/index.html',
                resolve: {
                    competition: function (CompetitionService) {
                        return CompetitionService.getActive();
                    }
                }
                /*
                controller: 'CompetitionController',
                templateUrl: 'static/app/templates/competition.html',
                resolve: {
                    competition: function (CompetitionService) {
                        return CompetitionService.getActive();
                    }
                }
                */
            })
            .when('/competition/:competition_id', {
                controller: 'CompetitionController',
                templateUrl: 'static/app/templates/competition.html',
                resolve: {
                    competition: function (CompetitionService, $route) {
                        return CompetitionService.getById($route.current.params.competition_id);
                    }
                }
            })
            .when('/questionnaire', {
                controller: 'QuestionnaireController',
                templateUrl: 'static/app/templates/questionnaire.html',
                resolve: {
                    questionnaire: function (QuestionnaireService) {
                        return QuestionnaireService.getActive();
                    }
                }
            })
            .when('/questionnaire/:questionnaire_id', {
                controller: 'QuestionnaireController',
                templateUrl: 'static/app/templates/questionnaire.html',
                resolve: {
                    competition: function (QuestionnaireService, $route) {
                        return QuestionnaireService.getById($route.current.params.questionnaire_id);
                    }
                }
            })
            .when('/company/:text_id', {
                controller: 'TextController',
                templateUrl: 'static/app/templates/text.html'
            })
            .when('/service/:text_id', {
                controller: 'TextController',
                templateUrl: 'static/app/templates/text.html'
            })
            .when('/winners/prizes/:code/', {
                controller: 'WinnerPrizeListController',
                controllerAs: 'vm',
                templateUrl: 'static/app/templates/prize-list-only-prizes.html',
                resolve: {
                }
            })
            .when('/winners/prize/:prize_id/', {
                controller: 'WinnerPrizeDetailController',
                templateUrl: 'static/app/templates/prize-detail.html'
            })
            .when('/winners/confirm', {
                controller: 'WinnerConfirmController',
                controllerAs: 'vm',
                templateUrl: 'static/app/templates/prize-confirm.html',
                resolve: {
                }
            })
            .when('/winners/tnx', {
                templateUrl: 'static/app/templates/prize-tnx.html',
                resolve: {
                }
            })
            .when('/shop', {
                controller: 'PrizeController',
                controllerAs: 'vm',
                templateUrl: 'static/app/templates/prize-list-only-prizes.html',
                resolve: {
                }
            })

            .when('/theatermediaclan', {
                controller: 'TheaterMediaClanController',
                controllerAs: 'vm',
                templateUrl: 'static/app/templates/theater-media-clan.html',
                resolve: {
                }
            })

            .when('/marketresearch', {
                controller: 'MarketResearchController',
                controllerAs: 'vm',
                templateUrl: 'static/app/templates/marketresearch.html',
                resolve: {
                }
            })

              .when('/colortrend', {
                controller: 'MarketResearchController',
                controllerAs: 'vm',
                templateUrl: 'static/app/templates/colortrend.html',
                resolve: {
                }
            })

            .when('/shop-old', {
                controller: 'CatalogController',
                controllerAs: 'vm',
                templateUrl: 'static/app/templates/prize-list.html',
                resolve: {
                    categories: function (CatalogService) {
                        return CatalogService.loadCategories();
                    },
                    competition: function (CompetitionService, $route) {
                        return CompetitionService.getActive();
                    }
                }
            })
            .when('/winners', {
                controller: 'WinnersController',
                controllerAs: 'vm',
                templateUrl: 'static/app/templates/winners.html',
                resolve: {
                }
            })
            .when('/competition/:competition_id/prizes', {
                controller: 'PrizeListController',
                controllerAs: 'vm',
                templateUrl: 'static/app/templates/prize-list.html',
                resolve: {
                    competition: function (CompetitionService, $route) {
                        return CompetitionService.getById($route.current.params.competition_id);
                    }
                }
            })
            .when('/competition/:competition_id/prize/:prize_id', {
                controller: 'CompetitionController',
                templateUrl: 'static/app/templates/competition.html',
                resolve: {
                    competition: function (CompetitionService, $route) {
                        return CompetitionService.getById($route.current.params.competition_id);
                    }
                }
            })
            .when('/competition/:competition_id/photo/:photo_id', {
                controller: 'CompetitionController',
                templateUrl: 'static/app/templates/competition.html',
                resolve: {
                    competition: function (CompetitionService, $route) {
                        return CompetitionService.getById($route.current.params.competition_id);
                    }
                }
            })
            .when('/prize/:prize_id/', {
                controller: 'PrizeDetailController',
                templateUrl: 'static/app/templates/prize-detail.html'
            })

            .when('/design/:design_id/', {
                controller: 'MarketResearchController',
                templateUrl: 'static/app/templates/market-research-detail.html'
            })

            .when('/select-photo-fb', {
                controller: 'FacebookSelectPhotoController',
                templateUrl: 'static/app/templates/select-photo.html',
                resolve: {
                    competition: function (CompetitionService) {
                        return CompetitionService.getActive();
                    },
                    'PhotoServiceData': function (PhotoService) {
                        // MyServiceData will also be injectable in your controller, if you don't want this you could create a new promise with the $q service
                        return PhotoService.promise;
                    }
                }
            })
            .when('/select-photo-ig', {
                controller: 'InstagramSelectPhotoController',
                templateUrl: 'static/app/templates/select-photo.html'
            })
            .when('/cart', {
                controller: 'CartController',
                controllerAs: 'vm',
                templateUrl: 'static/app/templates/cart.html',
                resolve: {
                    competition: function (CompetitionService) {
                        return CompetitionService.getActive();
                    }
                }
            })

            .when('/theatermediacart', {
                controller: 'CartController',
                controllerAs: 'vm',
                templateUrl: 'static/app/templates/theatermediacart.html',
                resolve: {
                    competition: function (CompetitionService) {
                        return CompetitionService.getActive();
                    }
                }
            })


            .when('/prizeCart', {
                controller: 'CartController',
                controllerAs: 'vm',
                templateUrl: 'static/app/templates/prizeCart.html',
                resolve: {
                    competition: function (CompetitionService) {
                        return CompetitionService.getActive();
                    }
                }
            })
            .when('/order/checkout', {
                controller: 'CheckoutOrderController',
                controllerAs: 'vm',
                templateUrl: 'static/app/templates/order-checkout.html'

            })
            .when('/order/confirm', {
                controller: 'ConfirmOrderController',
                controllerAs: 'vm',
                templateUrl: 'static/app/templates/order-confirm.html'

            })
            .when('/order/tnx', {
                controller: 'TnxOrderController',
                controllerAs: 'vm',
                templateUrl: 'static/app/templates/order-tnx.html'

            })
            .otherwise({
                redirectTo: '/'
            });

    }])
    .controller('ApplicationController', ['$scope', '$location', '$http', 'ezfb', 'Auth', 'ngCart', '$timeout', 'CompetitionService',
        function ($scope, $location, $http, ezfb, Auth, ngCart, $timeout, CompetitionService) {
            $scope.Auth = Auth;
            $scope.infoMessage = "";
            $scope.topCompetitionId = appConfig.topCompetitionId;
            $scope.ngCart = ngCart;
            $scope.competitionId = 0;
            $scope.competitionList = [];
            $scope.requireshipping = false;

            $scope.$on('ngCart:change', function(){
                //console.log(ngCart.getTotalItems());
                $scope.cartItemCount = ngCart.getTotalItems();
                $scope.updateCart($scope.requireshipping);
            });

            $scope.onFooterLoad = function () {
                /* Scroll to top*/
                $(window).scroll(function () {
                    if ($(document).scrollTop() < 100) {
                        $(".top-site").fadeOut('slow');
                    }
                    else {

                        $(".top-site").fadeIn('slow');

                    }
                });

                $(".top-site i").on('click', function () {
                    $("html, body").animate({
                        scrollTop: 0
                    }, 1000);
                });
            };

            $scope.onHeaderLoad = function() {
                //$.slidebars();
                $timeout(function() {
                    var mySlidebars = new $.slidebars();
                },1000);
            };

            $scope.showInfoMessage = function (infoMessage) {
                $scope.infoMessage = infoMessage;

                $('#info-popup').modal("show");
            };

            $scope.login = function (provider) {
                Auth.login(provider).then(function(ret) {
                    $timeout(function() {
                        console.log(Auth.isAuth(), ret);
                        appConfig.isAuth = true;
                        appConfig.avatar = ret.avatar;
                    },1000);
                });
                $('#signup-opt').modal("hide");
            };

            $scope.logout = function () {
                Auth.logout();
            };

            $scope.termsFlag = false;

            $scope.termsClick = function () {
                //console.log($scope.termsFlag, typeof $scope.termsFlag);
                if ($scope.termsFlag === true) {
                    Auth.updateTermsFlag();
                }
                else {
                    Auth.logout();
                }
                $('#terms-popup').modal("hide");
            };

            $scope.goToCart = function() {
                $("#success").modal('hide');
                $scope.go('/cart');
            };

            $scope.goToTheaterGroupCart = function() {
                $("#success").modal('hide');
                $scope.go('/theatermediacart');
            };

            $scope.go = function (path) {
                $timeout(function(){
                    $location.url(path);
                }, 100);
                $("#success").modal('hide');
                $('.modal').modal('hide');
            };

            $scope.myImage = '';
            $scope.myCroppedImage = '';

            $scope.uploadImage = function () {
                $('#photo-crop-popup').modal('hide');
                $('#spinner-mod').modal('show');

                $http({
                    method: 'POST',
                    url: '/upload_photo_from_src/',
                    data: $.param({'imgsrc': $scope.myCroppedImage, 'competition_id': $scope.competitionId}),
                    headers: {'Content-Type': 'application/x-www-form-urlencoded'}
                })
                .success(function (data, status, headers, config) {
                    var e = $('#fileUploadInput');
                    e.wrap('<form>').closest('form').get(0).reset();
                    e.unwrap();
                    $('#spinner-mod').modal('hide');
                    $location.url("/competition/" + data.competition_id + "/photo/" + data.photo_id);
                })
                .error(function(data, status, headers, config) {
                    $('#spinner-mod').modal('hide');
                    $scope.showInfoMessage("Error while photo upload, try again");
                });
            };

            $scope.updateCart = function(value) {
                console.log('update cart called.');
                
                if (!value){
                    ngCart.setShipping(0);    
                    console.log("Unsetting shipping to " + ngCart.getShipping());
                    $scope.requireshipping = false;
                }
                else
                {
                    ngCart.setShipping(ngCart.getTotalItems()*10);
                    console.log("Setting shipping to " + ngCart.getShipping());
                    $scope.requireshipping = true;
                }
                
            }

            $scope.showCropImagePopup = function(competitionId) {
                $scope.competitionId = competitionId;
                $('#photo-crop-popup').modal("show");
            };

            var handleFileSelect = function (evt) {
                var file = evt.currentTarget.files[0];
                var reader = new FileReader();
                console.log(file);

                $('#photo-crop-popup').modal("show");

                reader.onload = function (evt) {
                    $scope.$apply(function ($scope) {
                        $scope.myImage = evt.target.result;
                    });
                };
                reader.readAsDataURL(file);
            };

            $scope.selectPhotoFromDesktop = function (competitionId) {
                //console.log(Auth.isAuth());
                if(typeof competitionId != "undefined") {
                    return $scope.selectCompetitionForUpload(competitionId);
                }
                else {
                    $('#upload-popup').modal('show');
                }
            };

            $scope.selectCompetitionForUpload = function(competitionId) {
                $scope.competitionId = competitionId;
                $('#upload-popup').modal('hide');

                if (!Auth.isAuth()) {
                    Auth.showLoginPopup();
                }
                else {
                    $('#fileUploadInput').click();
                }
            };

            $scope.showProduct = function(id) {
                $('#spinner-mod').modal('show');
                $scope.$broadcast('productPopupOpen', id);
            };

            $scope.showWelcomeVideoPopup = function() {
                $('#welcome-video-popup').modal('show');
            };

            $scope.selectPhoto = function (provider, competitionId) {
                if ('facebook' == provider) {
                    ezfb.getLoginStatus().then(function (res) {
                        if(res.status == "connected") {
                            $location.url('/select-photo-fb?competition_id=' + competitionId);
                        }
                        else {
                            Auth.login(provider).then(function () {
                                    $location.url('/select-photo-fb?competition_id=' + competitionId);
                                },
                                function () {
                                    console.log('login canceled');
                                }
                            );
                        }
                    });
                }
                else if ('instagram' == provider) {
                    if (Auth.getAccessToken() !== '') {
                        return $location.url('/select-photo-ig?competition_id=' + competitionId);
                    }

                    if (appConfig.socialAuthProvider == 'instagram') {
                        Auth.loadAccessToken().then(function () {
                                $location.url('/select-photo-ig?competition_id=' + competitionId);
                            },
                            function (error) {
                                console.log(error);
                            }
                        );
                        return true;
                    }

                    Auth.login(provider, '/#!/select-photo-ig?competition_id=' + competitionId);
                }
            };

            function init(){
                CompetitionService.getActiveList().then(function (data) {
                    $scope.competitionList = data;
                });
            }

            //TODO: This code is temporarily commented out for debugging purposes. Uncomment it before
            //committing to bitbucket. If this is not uncommented, the main shopping system will not 
            //know which is the active competition and all hell will break loose.
            //init();
            angular.element(document.querySelector('#fileUploadInput')).on('change', handleFileSelect);
        }])
    .directive('productCarousel', function () {
        return function (scope, element, attrs) {
            if (scope.$last) {
                $(element).parent().flickity();
            }
        };
    })
    .directive('productSlickCarousel', function () {
        return function (scope, element, attrs) {
            if (scope.$last) {
                $(element).parent().slick();
            }
        };
    })
    .filter('encodeURIComponent', function () {
        return window.encodeURIComponent;
    })
    .filter('nl2br', ['$sce', function ($sce) {
        return function (msg, is_xhtml) {
            var is_xhtml = is_xhtml || true;
            var breakTag = (is_xhtml) ? '<br />' : '<br>';
            var msg = (msg + '').replace(/([^>\r\n]?)(\r\n|\n\r|\r|\n)/g, '$1' + breakTag + '$2');
            return $sce.trustAsHtml(msg);
        }
    }]);

function createCookie(name, value, days) {
    var expires;

    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toGMTString();
    } else {
        expires = "";
    }
    document.cookie = encodeURIComponent(name) + "=" + encodeURIComponent(value) + expires + "; path=/";
}

function readCookie(name) {
    var nameEQ = encodeURIComponent(name) + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) === ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) === 0) return decodeURIComponent(c.substring(nameEQ.length, c.length));
    }
    return null;
}

function eraseCookie(name) {
    createCookie(name, "", -1);
}
