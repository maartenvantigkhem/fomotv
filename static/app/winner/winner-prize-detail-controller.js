/**
 * Prize detail controller
 * for prize block on competition page and prize popup on catalog page
 */
(function () {
    'use strict';

    angular
        .module('mainApp')
        .controller('WinnerPrizeDetailController', WinnerPrizeDetailController);

    WinnerPrizeDetailController.$inject = ['$scope', '$controller', '$routeParams', '$cookies', '$location', '$timeout', 'ngCart', 'CatalogService', 'ezfb'];

    function WinnerPrizeDetailController($scope, $controller, $routeParams, $cookies, $location, $timeout, ngCart, CatalogService, ezfb) {
        //var pd = this;
        $controller('PrizeDetailController', {$scope: $scope}); //This works

        $scope.showPrice = false;

        $scope.selectPrize = function(selectedPrize) {
            $cookies.prize_id = selectedPrize.id;
            $location.url("/winners/confirm");
        };
    }

})();