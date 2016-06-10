/**
 * Prize detail controller
 * for prize block on competition page and prize popup on catalog page
 */
(function () {
    'use strict';

    angular
        .module('mainApp')
        .controller('PrizeDetailController', PrizeDetailController);

    PrizeDetailController.$inject = ['$scope', '$routeParams', '$cookies', '$location', '$timeout', 'ngCart', 'CatalogService', 'ezfb'];

    function PrizeDetailController($scope, $routeParams, $cookies, $location, $timeout, ngCart, CatalogService, ezfb) {
        //var pd = this;
        $scope.color = null;
        $scope.colorCode = null;
        $scope.size = null;
        $scope.photoCount = 0;

        $scope.currentUrl = $location.absUrl();
        $scope.shareName = "Prized.tv";
        $scope.shareText = "Win this on prized.tv";
        $scope.shareCaption = "prized.tv";

        $scope.showPrice = true;

        $scope.selectColor = function(color, colorCode) {
            $scope.color = color;
            $scope.colorCode = colorCode;

        };

        $scope.selectSize = function(size) {
            $scope.size = size;
            console.log(size);
        };

        $scope.addToCart = function (prize) {
            if (prize !== null) {

                if($scope.color == null) {
                    $scope.color = prize.colors[0].name;
                }

                if(prize.sizes.length ==  1) {
                    $scope.size = prize.sizes[0];
                }

                if($scope.size  == null) {
                    $scope.showInfoMessage("Please, select your size to continue");
                    return false;
                }

                var item = ngCart.getItemById(prize.id);

                var quantity = 1;
                if (item) {
                    quantity = item.getQuantity() + 1
                }

                console.log(prize.id);

                ngCart.addItem(prize.id,
                    prize.name,
                    prize.sale_price,
                    quantity,
                    {
                        'image': prize.thumbnail,
                        'size': $scope.size,
                        'color': $scope.color
                    });
                // Add to Bag Popup Start

                $("#success").modal('show');
            }
            else {
                //TODO: show error (no product selected)
            }

        };

        $scope.fbShare = function () {
            ezfb.ui(
                {
                    method: 'feed',
                    name: $scope.shareName,
                    picture: $scope.selectedPrize.photos[0].image,
                    link: $scope.currentUrl,
                    description: $scope.shareText,
                    caption: $scope.shareCaption
                },
                function (res) {
                }
            );
        };

        function init() {
            if (typeof $routeParams.prize_id == 'undefined') {
                return $location.url("/");
            }

            var id = $routeParams.prize_id;

            console.log(id);
            $scope.color = null;
            $scope.colorCode = null;
            $scope.size = null;

            CatalogService.loadProduct(id).then(function(product) {
                //$('#spinner-mod').modal('hide');

                $scope.selectedPrize = product;

                $timeout(function () {
                    $('.slider-for').slick({
                        slidesToShow: 1,
                        slidesToScroll: 1,
                        arrows: false,
                        fade: true,
                        asNavFor: '.slider-nav',
                        adaptiveHeight: true
                    });
                    $('.slider-nav').slick({
                        slidesToShow: 3,
                        slidesToScroll: 1,
                        asNavFor: '.slider-for',
                        dots: false,
                        centerMode: false,
                        focusOnSelect: true
                    });

                    //$('#product-detail').on('shown.bs.modal', function (e) {
                    //    $('.slider-for, .slider-nav').slick("setPosition", 0);
                    //});

                    Dropdown1();
                    //Color_Choose();
                    //Size_Choose();
                    Detail_Accordion();

                }, 1000);
            });

        }

        init();
    }




})();