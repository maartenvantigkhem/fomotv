/**
 * Controller for prize list on first page and competition page
 */
(function () {
    'use strict';

    angular
        .module('mainApp')
        .controller('PrizeController', PrizeController);

    PrizeController.$inject = ['$scope', 'CompetitionService', 'PrizeService'];

    function PrizeController($scope, CompetitionService, PrizeService) {
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
        }

        init();
    }
})();