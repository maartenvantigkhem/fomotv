/**
 * controller for Winners page
 */
(function () {
    'use strict';

    angular
        .module('mainApp')
        .controller('UserController', UserController);

    UserController.$inject = ['$scope', '$timeout', 'Auth'];

    function UserController($scope, $timeout, Auth) {
        var uc = this;
               
        uc.login = function login() {
            Auth.emailLogin(uc.email, uc.password). then(
                    function() {
                        console.log("ok");
                        uc.regFormError = "";
                    },
                    function() {
                        uc.regFormError = "Username / Password invalid";
                    }
                );
        }
        
        
        uc.register = function(isValid) {
            if(isValid) {
                Auth.register(uc.email, uc.password, uc.username).then(
                    function() {
                        console.log("ok");
                        uc.regFormError = "";
                    },
                    function() {
                        uc.regFormError = "Form validation error";
                    }
                );
            }
        };
    }
})();