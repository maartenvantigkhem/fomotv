/**
 * Market Research Controller
 */
(function() {
    'use strict';

    angular
        .module('mainApp')
        .controller('MarketResearchController', MarketResearchController);

    MarketResearchController.$inject = ['$scope', '$routeParams', '$location', '$timeout', 'MarketResearchService', '$cookies'];

    function MarketResearchController($scope, $routeParams, $location, $timeout, MarketResearchService, $cookies) {

        function init() {

            var tempCeil, tempFloor;

            //This is for the colorTrends
            MarketResearchService.getColorList().then(function(colors) {
                $scope.colors = colors;
            });

            //This is for the design trends
            MarketResearchService.getDesignTrends().then(function(designs) {
                $scope.designs = designs;
            });

            $scope.detailLink = "/#!/design/";

            //Do I need to create a new user - Check the cookies.
            $scope.username = $cookies.designtrendsusername;
            if ($scope.username == null) {
                //generate a random user name
                $scope.username = Math.random().toString(36).substring(7);
                $cookies.designtrendsusername = $scope.username; //Dump that username into a session cookie

                MarketResearchService.createNewUser($scope.username);
            }

            //Try to replace this jQuery code with an angular directive. -- TODO
            $('.heart-selected').hide();

            $scope.color = null;
            $scope.sizelist = [];
            $scope.selectedSize = null;
            $scope.colorCode = null;
            $scope.size = null;
            $scope.nps = 5;

            // Items in the Details Page only
            if (typeof $routeParams.design_id != 'undefined') {

                var id = $routeParams.design_id;

                MarketResearchService.loadDesign(id).then(function(design) {

                    $scope.selectedDesign = design;

                    //Prepare the Dropdown for the sizes
                    $scope.selectedDesign.sizes.forEach(function(data) {
                        $scope.sizelist.push(data.sizes);
                    });

                    //Check if the ceil is greater than the floor
                    if (design.ceil_cost > design.floor_cost) {
                        tempCeil = design.ceil_cost;
                        tempFloor = design.floor_cost;
                    } else {
                        tempCeil = design.floor_cost;
                        tempFloor = design.ceil_cost;
                    }

                    //Initial Options for the Price Slider
                    $scope.priceslider = {
                        value: 150,
                        options: {
                            ceil: tempCeil,
                            floor: tempFloor,
                            translate: function(value){
                                return '$' + value;
                            }
                        }
                    };

                    var npsStrings = [
                        "No",
                        "Unlikely",
                        "Maybe",
                        "Likely",
                        "Definitely"
                    ];

                    //Initial Options for the NPS Slider
                    $scope.npsslider = {
                        value: 2,
                        options: {
                            ceil: 4,
                            floor: 0,
                            translate: function(value){
                                return npsStrings[value];
                            }
                        }
                    };
                });
            }
        }

        $timeout(function() {
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

            Dropdown1();
            Detail_Accordion();

        }, 1000);

        $scope.castVote = function() {
            MarketResearchService.castVote(
                $scope.selectedDesign.design_ID,
                $scope.username,
                $scope.priceslider.value,
                $scope.npsslider.value+1,
                $scope.selectedSize
                ).then(
                    function(data){
                        $location.path("/marketresearch");
                    },
                    function(data){
                        console.log("Not Permitted. User Already Voted");
                        $location.path("/marketresearch");
                    }
                );
        };

        $scope.likeclick = function(id) {
            var hex = $scope.colors[id].color_hex;
            var name = $scope.colors[id].color_name;
            $('.heart-unselected' + hex).hide();
            $('.heart-selected' + hex).show();
            $scope.colors[id].up_votes++;
            MarketResearchService.UpdateLikes(hex, name, $scope.colors[id].up_votes);
        };

        $scope.unlikeclick = function(id) {
            var hex = $scope.colors[id].color_hex;
            var name = $scope.colors[id].color_name;
            $('.heart-selected' + hex).hide();
            $('.heart-unselected' + hex).show();
            $scope.colors[id].up_votes--;
            MarketResearchService.UpdateLikes(hex, name, $scope.colors[id].up_votes);
        };

        init();
    }
})();
