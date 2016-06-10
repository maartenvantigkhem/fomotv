/**
 * Order controller
 * Order Review and confirmation page
 */
(function () {
    'use strict';

    angular
        .module('mainApp')
        .controller('ConfirmOrderController', ConfirmOrderController)
        .controller('TnxOrderController', TnxOrderController);

    ConfirmOrderController.$inject = ['$scope', '$http', '$location', '$cookies', '$cookieStore', 'ngCart', 'OrderService'];

    function ConfirmOrderController($scope, $http, $location, $cookies, $cookieStore, ngCart, OrderService) {
        var vm = this;
        vm.ngCart = ngCart;
        vm.items = ngCart.getItems();
        vm.order_type = null;
        vm.order = null;

        function init() {
            var order_type = $cookies.order_type;

            if(order_type == "express") {
                var order = $cookies.order;
                order = order.replace(/\\054/g, ",");
                try {
                    vm.order = JSON.parse(JSON.parse(order));
                }
                catch(e) {
                    vm.order = {};
                }
            }

            if(order_type === "direct") {
                var order = globalOrder;
                vm.order = order;
            }

            if(typeof order == "undefined" || typeof order_type == "undefined") {
                //$location.url('/cart');
            }
            vm.order_type = order_type;
        }

        init();

        vm.confirmOrder = function() {
            if(vm.order_type == "direct") {
                vm.confirmDirectOrder();
            }
            else {
                vm.confirmExpressOrder();
            }
        };

        vm.confirmExpressOrder = function() {
            OrderService.confirmExpressCheckout(vm.order).then(function(data) {
                vm.order.id = data.data.order_id;
                $cookies.order = vm.order;
                $location.path("/order/tnx");
            });

        };

        vm.confirmDirectOrder = function() {
            var cart = ngCart.getCart();
            $cookies.cart = JSON.stringify(cart);

            OrderService.confirmDirectCheckout(vm.order).then(function(data) {
                vm.order.id = data.data.order_id;
                $cookies.order = vm.order;
            });
        };

        vm.cancelOrder = function() {
            $cookieStore.remove('order');
            $cookieStore.remove('order_type');
            $location.url("/cart");
          }
    }

    TnxOrderController.$inject = ['$scope', 'ngCart'];

    function TnxOrderController($scope, ngCart) {
        var vm = this;

        function init(){
            ngCart.empty(true);
            $scope.cartItemCount = 0;
        }

        init();
    }
})();