/**
 * Order Service. Confirmation functions
 */
(function () {
    'use strict';

    angular
        .module('mainApp')
        .service('OrderService', OrderService);

    OrderService.$inject = ['$http'];

    function OrderService($http) {

        function confirmExpressCheckout(order) {
            console.log ("In ConfirmExpressCheckout: Token:  " + order.token);
            return $http({
                method: 'GET',
                url: '/order/paypal/end'+"?token="+order.token,
                data: "token=" + order.token,
                headers: {'Content-Type': 'application/x-www-form-urlencoded'}
            }).then(
                function(data){
                    if(typeof data.data.error != "undefined") {
                        console.log(data.data.error);
                        }
                    return data;
                    },
                function(data) {});
            }

        function confirmDirectCheckout(order) {
            var order_str = JSON.stringify(order);

            return $http({
                method: 'GET',
                url: '/order/save'+"?order=" + order_str,
                data: "order=" + order_str,
                headers: {'Content-Type': 'application/x-www-form-urlencoded'}
            }).then(
                function(data){

                    if(typeof data.data.error != "undefined") {
                        console.log(data.data.error);
                        }
                    return data;
                    },function(data) {});
            }
        return {
            confirmExpressCheckout: confirmExpressCheckout,
            confirmDirectCheckout: confirmDirectCheckout
        }

    }
})();