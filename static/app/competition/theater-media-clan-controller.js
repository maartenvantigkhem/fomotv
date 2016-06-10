/**
 * Controller for prize list on first page and competition page
 */
(function () {
    'use strict';

    angular
        .module('mainApp')
        .controller('TheaterMediaClanController', TheaterMediaClanController);

    TheaterMediaClanController.$inject = ['$scope', 'CompetitionService', 'PrizeService', 'ngCart'];

    function TheaterMediaClanController($scope, CompetitionService, PrizeService, ngCart) {
        $scope.competition = CompetitionService.getCompetition();
        $scope.prizes = [];
        $scope.showPrice = true;
        $scope.detailLink = "/#!/prize/";

        $scope.getPrizes = function () {
            return $scope.prizes; //PrizeService.getCurrentWeekList();
        };

        function init() {
            PrizeService.getCurrentWeekList().then(function(data) {
                $scope.prizes = data;
            })
        };

        init();


        $scope.addToCart = function (prize) {
            if (prize !== null) {
                if($scope.color == null) {
                    $scope.color = prize.colors[0].name;
                }

                $scope.size = 'S';

                var item = ngCart.getItemById(prize.id);

                var quantity = 1;
                if (item) {
                    quantity = item.getQuantity() + 1
                }

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

    }
})();