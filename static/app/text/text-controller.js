/**
 * controller for Text pages
 */
(function () {
    'use strict';

    angular
        .module('mainApp')
        .controller('TextController', TextController);

    TextController.$inject = ['$scope', '$routeParams'];

    function TextController($scope, $routeParams) {
        $scope.active_text = null;

        function init() {
            if (typeof $routeParams.text_id != 'undefined') {
                $scope.active_text = $routeParams.text_id;
            }
            else {
                $scope.active_text = "aboutus";
            }
        }

        init();

    }
})();