(function () {
    'use strict';

    angular
        .module('mainApp')
        .controller('CartController', CartController);

    CartController.$inject = ['$scope', '$location', '$cookies', 'ngCart', 'CompetitionService'];

    /**
     * Controller for cart page
     *
     * @param $scope
     * @param $location
     * @param $cookies
     * @param ngCart
     * @param CompetitionService
     * @constructor
     */
    function CartController($scope, $location, $cookies, ngCart, CompetitionService) {
        var vm = this;
        vm.ngCart = ngCart;
        vm.competition = CompetitionService.getCompetition();
        vm.items = ngCart.getItems();
        $scope.hideCartFlag = true;

        vm.goToPaypalStart = function() {
            var cart = ngCart.getCart();
            var jsonCart = JSON.stringify(cart);

            $cookies.cart = jsonCart;

            window.location = "/order/paypal/start";

            //$location.path = "/order/paypal/start";
        }

        vm.goToCheckout = function() {
            $location.url("/order/checkout");
        }

        vm.decreaseQuantity = function(item) {
            item.setQuantity(-1, true);
        }
    }
})();