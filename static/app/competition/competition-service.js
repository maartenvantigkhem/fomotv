/**
 * Competition service
 */
(function () {
    'use strict';

    angular
        .module('mainApp')
        .service('CompetitionService', CompetitionService);

    CompetitionService.$inject = ['$http'];

    function CompetitionService($http) {
        var competition = null;
        var competition_list = null;
        var prizes = null;
        var photos = null;

        function getActiveList() {
            return $http.get('/api/v1/competitions?active_flag=True&page_size=3')
            .then(
                function (res) {

                    competition_list = res.data.results;
                    console.log(res, competition_list);
                    return competition_list;
                },
                function (res) {
                    console.log('error competition list loading');
                }
            );
        }

        function getFinishedList() {
            return $http.get('/api/v1/competitions?end_flag=True')
            .then(
                function (res) {
                    competition_list = res.data;
                    console.log(res.data);
                    return competition_list;
                },
                function (res) {
                    console.log('error competition list loading');
                }
            );
        }

        function getActive() {
            return $http.get('/api/v1/competitions/top')
            .then(
                function (res) {
                    competition = res.data
                    prizes = res.data.prizes;
                },
                function (res) {
                    console.log('error competition loading');
                }
            );
        }

        function getById(id) {
            return $http.get('/api/v1/competitions/' + id)
            .then(
                function (res) {
                    competition = res.data
                    prizes = res.data.prizes;
                },
                function (res) {

                    console.log('error competition loading');
                }
            );
        }

        function loadPhotos(competitionId, photoId) {
            var photoUrl = '/api/v1/photos?competition_id='+competitionId + '&photo_id=' + photoId;

            return $http.get(photoUrl, {cache: false})
                .then(function (res) {
                    photos = res.data.results;
                    return photos;
                },
                function (res) {
                    console.log(res, 'error photo loading');
                });
        }

        function setFirstPhoto(photoId) {
            var index = photos.map(function(x) {return x.id; }).indexOf(parseInt(photoId));
            if(index > -1) {
                var temp = photos[0];
                photos[0] = photos[index];
                photos[index] = temp;
            }
        }

        function getPrizeById(prizeId) {
            if (prizes == null) return null;
            
            var result = $.grep(prizes, function (e) {
                return e.id == prizeId;
            });

            if (result.length == 1) {
                return result[0];
            }
            else {
                return null;
            }
        }

        function getFirstPrize() {
            if (prizes != null) return prizes[0];
            else return null;
        }

        function vote(photoId, competitionId, score) {
            return $http.get('/photo/vote?photoId=' + photoId + '&competitionId=' + competitionId + '&score=' + score);
        }

        function share(photoId, competitionId) {
            return $http.get('/photo/share?photoId=' + photoId + '&competitionId=' + competitionId);
        }

        function abuse(photoId, type) {
            return $http.get('/api/v1/photos/' + photoId + '/abuse?type=' + type)
                .then(
                function (res) {

                },
                function (res) {

                }
            );
        }

        function cleanViewHistory(competitionId) {
            return $http.get('/api/v1/competitions/' + competitionId + '/clean_view_history/');
        }

        return {
            //promise: promise,
            getActiveList: getActiveList,
            getById: getById,
            loadPhotos: loadPhotos,
            getPrizes: function () {
                return prizes;
            },
            getPhotos: function () {
                return photos;
            },
            getCompetition: function () {
                return competition
            },
            getActive: getActive,
            getPrizeById: getPrizeById,
            getFirstPrize: getFirstPrize,
            vote: vote,
            share: share,
            abuse: abuse,
            setFirstPhoto: setFirstPhoto,
            getFinishedList: getFinishedList,
            cleanViewHistory: cleanViewHistory
        };
    }

})();
