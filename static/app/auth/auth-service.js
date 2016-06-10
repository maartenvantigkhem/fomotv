/**
 *
 * Auth service
 * Login/log out, terms popup, FB login etc
 *
 */

(function () {
    'use strict';

    angular
        .module('mainApp')
        .factory('Auth', Auth);

    Auth.$inject = ['$cookies','$http', 'ezfb'];

    /**
     *
     *
     * @namespace Auth
     * @returns {Factory}
     */
    function Auth($cookies, $http, ezfb) {
        /**
         * @name Authentication
         * @desc The Factory to be returned
         */
        var Auth = {
            getAuthenticatedAccount: getAuthenticatedAccount,
            isAuthenticated: isAuthenticated,
            setAuthenticatedAccount: setAuthenticatedAccount,
            unauthenticate: unauthenticate,
            register: register,
            emailLogin: emailLogin,
            isAuth: isAuth,
            getSocialAuthProvider: getSocialAuthProvider,
            setSocialAuthProvider: setSocialAuthProvider,
            setAuth: setAuth,
            getUsername: getUsername,
            getUserAvatar: getUserAvatar,
            login: login,
            logout: logout,
            getAccessToken: getAccessToken,
            loadAccessToken: loadAccessToken,
            getSocialUserId: getSocialUserId,
            showLoginPopup: showLoginPopup,
            showTermsPopup: showTermsPopup,
            updateTermsFlag: updateTermsFlag,
            checkTermsFlag: checkTermsFlag
        };

        return Auth;

        ////////////////////

        //Upon clicking the login button on the homepage, this method is called.
        function login(provider, next){
            if(provider == 'facebook'){
                //var next = document.location.href;

                //window.open('https://www.facebook.com/dialog/oauth?client_id='+appConfig.facebookAppId+
                //    '&redirect_uri='+  +'&scope=email,user_photos', '', null);

                if(navigator.userAgent.match('CriOS')) {
                    window.location = "/login/facebook?next=/";
                    return;
                }
                //    window.open('https://www.facebook.com/dialog/oauth?client_id='                        +appConfig.facebookAppId+                        '&redirect_uri='+ document.location.href +'&scope=email,user_photos', '', null);


                return ezfb.login(null, {scope: 'email,user_photos'}).then(function (res) {
                      /**
                       * no manual $scope.$apply, I got that handled
                       */
                      
                      // VIKRAM - First call /ajax-auth/ in common.py which will trigger the SocialAuth worklflow.
                      // The socialAuth workflow will trigger the SocialAuth pipeline that will populate the return response
                      // with the data that we are looking for here. Now go to common.py, search for ajax_auth and follow on from there.
                      if (res.authResponse) {
                        return $.getJSON('/ajax-auth/facebook/?access_token=' + res.authResponse['accessToken'], function(response){
                              appConfig.username = response.username;
                              appConfig.avatar = response.avatar;
                              appConfig.isAuth = true;
                              appConfig.socialAuthProvider = 'facebook';
                              appConfig.socialUserId = response.social_user_id;
                              appConfig.termsFlag = response.terms_flag

                              //$('#login-popup').popup("hide");

                              if(appConfig.termsFlag === false) {
                                  showTermsPopup();
                              }
                              return appConfig;
                          });
                          //updateLoginStatus(updateApiMe);
                      }
                });
            }

            if(provider == 'instagram'){
                if(!next) next = location.href;
                window.location = '/login/instagram?next=' + next;
            }
            return true;
        }

        function showTermsPopup() {
            $('#terms-popup').modal("show");
        }

        function checkTermsFlag() {
            if(appConfig.isAuth && appConfig.termsFlag === false) {
                showTermsPopup();
            }
        }

        function updateTermsFlag() {
            appConfig.termsFlag = true;
            return $http.post('/api/v1/auth/update-terms-flag/');

        }

        function logout() {
            appConfig.isAuth = false;
            appConfig.username = '';
            appConfig.socialAuthProvider = '';
            appConfig.socialUserId = ''
            appConfig.termsFlag = false;

            return $http.post('/api/v1/auth/logout/')
                .then(logoutSuccessFn, logoutErrorFn);
        }

        /**
         * @name logoutSuccessFn
         * @desc Unauthenticate and redirect to index with page reload
         */
        function logoutSuccessFn(data, status, headers, config) {
            //Authentication.unauthenticate();

            appConfig.isAuth = false;
            appConfig.username = '';
            appConfig.socialAuthProvider = '';
            appConfig.socialUserId = ''
            appConfig.termsFlag = false;
        }

        /**
         * @name logoutErrorFn
         * @desc Log "Epic failure!" to the console
         */
        function logoutErrorFn(data, status, headers, config) {
            console.error('Epic failure!');
        }

        function getUsername() {
            return appConfig.username;
        }

        function getUserAvatar() {
            return appConfig.avatar;
        }

        function isAuth() {
            return appConfig.isAuth;
        }

        function setAuth(authFlag) {
            appConfig.isAuth = authFlag;
        }

        function getSocialAuthProvider() {
            return appConfig.socialAuthProvider;
        }

        function setSocialAuthProvider(socialAuthProvider) {
            appConfig.socialAuthProvider = socialAuthProvider;
        }

        function getAccessToken() {
            return appConfig.accessToken;
        }

        function loadAccessToken() {
            return $http.get('/api/v1/auth/get-access-token/')
                .then(function(data, status, headers, config) {
                    appConfig.accessToken = data.data.access_token;
                    console.log(data.data.access_token)
                },
                function(error){
                    console.log('get auth token error');
                    throw error;
                }
            );
        }

        function getSocialUserId() {
            return appConfig.socialUserId;
        }

          /**
           * Update loginStatus result
           */
        function updateLoginStatus (more) {
            return ezfb.getLoginStatus(function (res) {
              $scope.loginStatus = res;

              (more || angular.noop)();
            });
        }

          /**
           * Update api('/me') result
           */
        function updateApiMe () {
            ezfb.api('/me', function (res) {
              $scope.apiMe = res;
            });
        }

        function showLoginPopup(){
            $('#signup-opt').modal("show");
        }

        /**
         * @name login
         * @desc Try to log in with email `email` and password `password`
         * @param {string} email The email entered by the user
         * @param {string} password The password entered by the user
         * @returns {Promise}
         * @memberOf thinkster.authentication.services.Authentication
         */
        function emailLogin(email, password) {
          return $http.post('/api/v1/auth/login/', {
            email: email,
            password: password
          }).then(loginSuccessFn, loginErrorFn);
        
          /**
           * @name loginSuccessFn
           * @desc Set the authenticated account and redirect to index
           */
          function loginSuccessFn(data, status, headers, config) {
            setAuthenticatedAccount(data.data);
            window.location = '/';
          }
        
          /**
           * @name loginErrorFn
           * @desc Log "Epic failure!" to the console
           */
          function loginErrorFn(data, status, headers, config) {
            console.error('Epic failure!');
            window.location = "/";
            }
        }

        
        /**
         * @name getAuthenticatedAccount
         * @desc Return the currently authenticated account
         * @returns {object|undefined} Account if authenticated, else `undefined`
         * @memberOf thinkster.authentication.services.Authentication
         */
        function getAuthenticatedAccount() {
          if (!$cookies.authenticatedAccount) {
            return;
          }
        
          return JSON.parse($cookies.authenticatedAccount);
        }
        
        /**
         * @name isAuthenticated
         * @desc Check if the current user is authenticated
         * @returns {boolean} True is user is authenticated, else false.
         * @memberOf thinkster.authentication.services.Authentication
         */
        function isAuthenticated() {
          return !!$cookies.authenticatedAccount;
        }
        
        /**
        * @name setAuthenticatedAccount
        * @desc Stringify the account object and store it in a cookie
        * @param {Object} user The account object to be stored
        * @returns {undefined}
        * @memberOf thinkster.authentication.services.Authentication
        */
       function setAuthenticatedAccount(account) {
         $cookies.authenticatedAccount = JSON.stringify(account);
       }
       
        /**
         * @name unauthenticate
         * @desc Delete the cookie where the user object is stored
         * @returns {undefined}
         * @memberOf thinkster.authentication.services.Authentication
         */
        function unauthenticate() {
          delete $cookies.authenticatedAccount;
        }
        
        /**
         * @name register
         * @desc Try to register a new user
         * @param {string} username The username entered by the user
         * @param {string} password The password entered by the user
         * @param {string} email The email entered by the user
         * @returns {Promise}
         * @memberOf thinkster.authentication.services.Authentication
         */
        function register(email, password, username) {
            return $http.post('/api/v1/user/', {
                username: username,
                password: password,
                email: email
            }).then(registerSuccessFn, registerErrorFn);
        }
        
        /**
        * @name registerSuccessFn
        * @desc Log the new user in
        */
        function registerSuccessFn(data, status, headers, config) {
            window.location = "/";
            showTermsPopup();
            
        }
      
        /**
        * @name registerErrorFn
        * @desc Log "Epic failure!" to the console
        */
        function registerErrorFn(data, status, headers, config) {
          console.error('Epic failure!');
          window.location = "/";
        }
    }
})();