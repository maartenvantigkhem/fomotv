/**
 * controller for Winners page
 */
(function () {
    'use strict';

    angular
        .module('mainApp')
        .controller('WinnersController', WinnersController);

    WinnersController.$inject = ['$scope', '$timeout', 'CompetitionService'];

    function WinnersController($scope, $timeout, CompetitionService) {
        $scope.competition_list = null;
        load_competition_list();

        function load_competition_list() {
            return CompetitionService.getFinishedList().then(function (data) {
                $scope.competition_list = data;
                console.log(data);
            });
        }

        $scope.convertDate = function(strDate) {
            // Split timestamp into [ Y, M, D, h, m, s ]
            var t = strDate.split(/[- :]/);

            // Apply each element to the Date function
            var d = new Date(t[0], t[1]-1, t[2]);

            return d.format("mediumDate");
        };

        $scope.showPrizes = function(index) {
            $scope.competition_list[index].show_prizes = true;
            $('.items-best-prize').slick();
            $('.items-best-prize').slick('slickGoTo', 0);
        };

        $scope.showPhoto = function(index) {
            $scope.competition_list[index].show_prizes = false;
        };
    }
})();