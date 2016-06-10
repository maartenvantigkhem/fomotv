/**
 * Checkout controller for order checkout page
 *
 */
(function () {
    'use strict';

    angular
        .module('mainApp')
        .controller('WinnerConfirmController', WinnerConfirmController);

    WinnerConfirmController.$inject = ['$scope', '$location', '$cookies', '$cookieStore', '$timeout', 'PrizeService'];

    function WinnerConfirmController($scope, $location, $cookies, $cookieStore, $timeout, PrizeService) {
        var vm = this;
        vm.countries = country_codes;
        vm.order = {};

        vm.confirm = function(isValid) {
            if(isValid) {

                console.log(vm.order.country);

                if(vm.order.country !== null)  {
                    vm.order.country_code = country_codes[vm.order.country].code;
                    vm.order.country_name = country_codes[vm.order.country].name;
                }
                vm.order.prize_id = $cookies.prize_id;
                vm.order.code = $cookies.winner_code;

                PrizeService.sendWinnerPrizeConfirmation(vm.order).then(function(data) {
                    console.log(data);
                    $cookieStore.remove('winner_code');
                    $cookieStore.remove('prize_id');
                    $location.url("/winners/tnx");
                },
                function(data) {
                    console.log(data);
                    //error
                });
            }
        };

        vm.cancelConfirmation = function() {
            $cookieStore.remove('prize_id');
            $location.url("/winners/prizes/" + $cookies.winner_code + "/");
        };

        function init() {
            if(!$cookies.hasOwnProperty("winner_code")) {
                return $location.url("/");
            }

            $timeout(function () {
                window.prettyPrint && prettyPrint();

                [].slice.call( document.querySelectorAll( 'select.cs-select' ) ).forEach( function(el) {
					new SelectFx(el, {
                      onChange: function(val) {
                        vm.order[el.name] = val;
                      }
                    });
				} );

            }, 10);
        }

        init();
    }

})();


