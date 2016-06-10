/**
 * Market Research Service
 */
(function() {
    'use strict';

    angular
        .module('mainApp')
        .service('MarketResearchService', MarketResearchService);

    MarketResearchService.$inject = ['$http'];

    function MarketResearchService($http) {
        var color_list = null;

        function createUser() {
            return $http.get('/api/v1/designtrend')
                .then(
                    function(res) {
                        return res.data;
                    },
                    function(res) {
                        console.log("Could not retreive design trends");
                    });
        }     

        function getDesignTrends() {
            return $http.get('/api/v1/designtrend')
                .then(
                    function(res) {
                        return res.data;
                    },
                    function(res) {
                        console.log("Could not retreive design trends");
                    });
        }

        function loadDesign(id) {
            return $http.get('/api/v1/designtrend/' + id)
                .then(
                    function(res) {
                        return res.data;
                    },
                    function(res) {
                        console.log("Could not retreive design trends");
                    });
        }

        function getColorList() {
            return $http.get('/api/v1/colortrend')
                .then(
                    function(res) {
                        return res.data;
                    },
                    function(res) {
                        console.log("Could not retrieve color list.");
                    });
        }

        function UpdateLikes(hex, name, upvotes) {
            return $http({
                method: 'PUT',
                url: '/api/v1/colortrend/' + hex + '/',
                data: {
                    "color_name": name,
                    "color_hex": hex,
                    "up_votes": upvotes,
                    "down_votes": 0
                },
                headers: {
                    'Content-Type': 'application/json'
                }
            });
        }

        function castVote(designid, username, howmuch, nps, preferredSize ){
            console.log(designid);
            console.log(username);
            console.log(howmuch);
            console.log(nps);
            console.log(preferredSize);
            return $http({
                method: 'POST',
                url: '/api/v1/uservotingtrend/',
                data: {
                    "design_ID": designid,
                    "user_id": username,
                    "how_much": howmuch,
                    "nps" : nps,
                    "preferred_size" : preferredSize
                },
                headers: {
                    'Content-Type': 'application/json'
                }
            });
        }

        function getUserLocation(){
            return $http.get('http://freegeoip.net/json/')
                .then(
                    function(res){
                        return res.data;
                    },
                    function(res){
                        console.log("Could not determine user's country");
                    });
        }   

        function addUser(username, userip, usercountry) {
            console.log("Add User Called");
            return $http({
                method: 'POST',
                url: '/api/v1/useridtrend/',
                data: {
                    "user_id": username,
                    "voter_ip": userip,
                    "voter_country": usercountry
                },
                headers: {
                    'Content-Type': 'application/json'
                }
            });
        }

        function createNewUser(username){

            //get the user's location:
            console.log("Inside createNewUser");
            getUserLocation()
                .then(function(userLocation){
                    addUser(username, userLocation.ip, userLocation.country_name);
                });
        }

        return {
            getColorList: getColorList,
            UpdateLikes: UpdateLikes,
            getDesignTrends: getDesignTrends,
            loadDesign: loadDesign,
            getUserLocation: getUserLocation,
            addUser: addUser,
            createNewUser: createNewUser,
            castVote: castVote
        };
    }

})();
