/**
 * controller for Winners page
 *
 * ---- I DONT THINK THIS FILE IS USED ANYWHERE. SEE REG-CONTROLLER.JS
 */
(function () {
    'use strict';

    angular
        .module('mainApp')
        .controller('AuthController', AuthController);

    AuthController.$inject = ['$scope', '$timeout', 'Auth'];

    function AuthController($scope, $timeout, Auth) {
        var uc = this;

        uc.login = login;
        //activate();
        
        /**
        * @name activate
        * @desc Actions to be performed when this controller is instantiated
        * @memberOf thinkster.authentication.controllers.LoginController
        */
        function activate() {
          // If the user is authenticated, they should not be here.
          if (Auth.isAuthenticated()) {
            $location.url('/');
          }
        }
    
        /**
        * @name login
        * @desc Log the user in
        * @memberOf thinkster.authentication.controllers.LoginController
        */
        uc.login = function login() {
            console.log("Calling uc.login in Auth Controller")
          Auth.emailLogin(uc.email, uc.password);
        }

        uc.register = function(isValid) {
            if(isValid) {
                Auth.register(uc.email, uc.password, uc.username).then(
                    function() {
                        console.log("ok");
                        uc.regFormError = ""
                    },
                    function() {
                        uc.regFormError = "Form validation error";
                        //console.log("reg error");
                    }
                );
            }
        };
    }
})();