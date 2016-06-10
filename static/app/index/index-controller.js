/**
 * Index controller for main page *
 *
 */
(function () {
    'use strict';

    angular
        .module('mainApp')
        .controller('IndexController', IndexController);

    IndexController.$inject = ['$scope', '$timeout', 'CompetitionService',];

    function IndexController($scope, $timeout, CompetitionService) {
        //get current active competition
        $scope.competition = CompetitionService.getCompetition();
        $scope.competitionList = null;

        loadCompetitionList();

        function loadCompetitionList() {
            return CompetitionService.getActiveList().then(function (data) {
                $scope.competitionList = data;

                $timeout(function () {
                    $('.captions').flowtype();

                }, 100);
            });
        }

        function showWelcomeVideoOnLoad() {
            if(readCookie("welcomeVideoViewed") == null) {
                $scope.showWelcomeVideoPopup();
                createCookie("welcomeVideoViewed", true, 365);
            }

            //$("#registration-popup").modal("show");
        }

        showWelcomeVideoOnLoad();
    }
})();