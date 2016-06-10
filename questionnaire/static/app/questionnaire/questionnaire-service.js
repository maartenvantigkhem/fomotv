/**
 * Competition service
 */
(function () {
    'use strict';

    angular
        .module('mainApp')
        .service('QuestionnaireService', QuestionnaireService);

    QuestionnaireService.$inject = ['$http'];

    function QuestionnaireService($http) {
        var questionnaire = null;
        var questionnaire_list = null;
        var prizes = null;
        var photos = null;

        function getActiveList() {
            return $http.get('/api/v1/questionnaire?active_flag=True&top_flag=False')
            .then(
                function (res) {
                    questionnaire_list = res.data.results;
                    return questionnaire_list;
                    //console.log(competition_list);

                },
                function (res) {
                    console.log('error questionnaire list loading');
                }
            );
        }

        //list on quizzes user not finished
        function getListForUser() {
            return $http.get('/api/v1/questionnaire/questionnaire_for_user/')
            .then(
                function (res) {
                    questionnaire_list = res.data;
                    return questionnaire_list;
                    //console.log(competition_list);
                },
                function (res) {
                    console.log('error questionnaire list loading');
                }
            );
        }

        function getFinishedList() {
            return $http.get('/api/v1/questionnaire?end_flag=True')
            .then(
                function (res) {
                    questionnaire_list = res.data;
                    console.log(res.data);
                    return questionnaire_list;
                    //console.log(competition_list);

                },
                function (res) {
                    console.log('error questionnaire list loading');
                }
            );
        }

        function getActive() {
            return $http.get('/api/v1/questionnaire/top')
            .then(
                function (res) {
                    questionnaire = res.data
                    prizes = res.data.prizes;
                    //console.log(competition)
                    //console.log(prizes)

                },
                function (res) {
                    console.log('error questionnaire loading');
                }
            );
        }

        function getById(id) {
            return $http.get('/api/v1/questionnaire/' + id)
            .then(
                function (res) {
                    questionnaire = res.data
                    prizes = res.data.prizes;
                    //console.log(competition)
                    //console.log(prizes)

                },
                function (res) {

                    console.log('error questionnaire loading');
                }
            );
        }

        function getPrizeById(prizeId) {
            //console.log(prizes, prizeId);

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

        function save_answer(questionId, score) {
            return $http.get('/questionnaire/save_answer?questionId=' + questionId + '&score=' + score)
                .then(
                function (res) {
                    return res;
                },
                function (res) {
                    console.log(res);
                }
            );
        }

        function getResult(questionnaireId) {
            return $http.get('/questionnaire/get_result?questionnaireId=' + questionnaireId)
                .then(
                function (res) {
                    return res;
                },
                function (res) {
                    console.log(res);
                }
            );
        }

        function share(photoId) {
            $http.get('/photo/share?photoId=' + photoId)
                .then(
                function (res) {

                },
                function (res) {

                }
            );
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

        return {
            //promise: promise,
            getActiveList: getActiveList,
            getById: getById,
            getPrizes: function () {
                return prizes;
            },
            getQuestionnaire: function () {
                return questionnaire;
            },
            getActive: getActive,
            getPrizeById: getPrizeById,
            getFirstPrize: getFirstPrize,
            save_answer: save_answer,
            share: share,
            abuse: abuse,
            getFinishedList: getFinishedList,
            getResult: getResult,
            getListForUser: getListForUser
        };
    }

})();
