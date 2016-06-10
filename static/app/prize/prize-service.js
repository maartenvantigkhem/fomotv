/**
 * Prize service
 */
(function () {
    'use strict';

    angular
        .module('mainApp')
        .service('PrizeService', PrizeService);

    PrizeService.$inject = ['$http'];

    function PrizeService($http) {
        var prizes = null;

        function getCurrentWeekList() {
            return $http.get('/api/v1/prizegroup/?group__code=current')
            .then(
                function (res) {
                    prizes = res.data;
                    //console.log(prizes);
                    return prizes;
                },
                function () {
                    console.log('error prizes list loading');
                }
            );
        }

        function getWinner(code) {
            return $http.get('/api/v1/winner/?code='+code)
            .then(
                function (res) {
                    var winner = res.data;
                    console.log(winner);

                    if(winner.length == 1) {
                        return winner[0];
                    }
                    //console.log(prizes);
                    return null;
                },
                function () {
                    console.log('error prizes list loading');
                }
            );
        }

        function getWinnerList(code) {
            return $http.get('/api/v1/prizegroup/winner/?code='+code)
            .then(
                function (res) {
                    prizes = res.data;
                    //console.log(prizes);
                    return prizes;
                },
                function () {
                    console.log('error prizes list loading');
                }
            );
        }

        function sendWinnerPrizeConfirmation(confirmation) {
            return $http({
                    method: 'POST',
                    url: '/api/v1/winner/confirm/',
                    data: $.param(confirmation),
                    headers: {'Content-Type': 'application/x-www-form-urlencoded'}
                });
        }

        return {
            getCurrentWeekList: getCurrentWeekList,
            getPrizes: function () {
                return prizes;
            },
            getWinnerList: getWinnerList,
            getWinner: getWinner,
            sendWinnerPrizeConfirmation: sendWinnerPrizeConfirmation
        };
    }

})();
