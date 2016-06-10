/**
 * Load Albums from Facebook for select photo page
 */
(function () {
    'use strict';

    angular
        .module('mainApp')
        .service('PhotoService', PhotoService);

    PhotoService.$inject = ['ezfb'];

    function PhotoService(ezfb) {
        var albums = null;

        var promise = ezfb.getLoginStatus()
            .then(function (res) {
                return ezfb.api('/me/albums');
            })
            .then(function (res) {
                albums = res.data;
            });

        return {
            promise: promise,
            getAlbums: function () {
                return albums;
            }
        };
    }

})();