/**
 * controller for Winners prize list
 */
(function () {
    'use strict';

    angular
        .module('mainApp')
        .controller('WinnerPrizeListController', WinnerPrizeListController);

    WinnerPrizeListController.$inject = ['$scope', '$routeParams', '$location', '$cookies', 'CompetitionService', 'PrizeService'];

    function WinnerPrizeListController($scope, $routeParams, $location, $cookies, CompetitionService, PrizeService) {
        $scope.competition = CompetitionService.getCompetition();
        $scope.prizes = [];
        $scope.showPrice = false;
        $scope.detailLink = "/#!/winners/prize/";

        $scope.getPrizes = function () {
            return $scope.prizes;
        };

        function init() {
            if (typeof $routeParams.code != 'undefined') {
                PrizeService.getWinner($routeParams.code).then(function(winner) {
                    if(winner !== null) {
                        if(winner.prize !== null) {
                            $location.url("/winners/tnx");
                        }
                        else
                        {
                            // save code in cookie
                            $cookies.winner_code = $routeParams.code;

                            PrizeService.getWinnerList($routeParams.code).then(function(data) {
                                $scope.prizes = data;
                            });
                        }
                    }
                    else
                    {
                        $location.url("/");
                    }
                });

            }

        }

        init();
    }
})();