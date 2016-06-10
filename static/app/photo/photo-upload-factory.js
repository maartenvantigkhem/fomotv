/**
 * Load Albums from Facebook for select photo page
 */
(function () {
    'use strict';

    angular
        .module('mainApp')
        .service('PhotoUploadFactory', PhotoUploadFactory);

    PhotoUploadFactory.$inject = [];

    function PhotoUploadFactory() {
        function Uploader(name) {
            this.name = name;
        }

        Uploader.prototype.getName = function() {
            return this.name;
        };

        Uploader.build = function (name) {
            return new Uploader(
                name
            );
        };

        return Uploader;
    }

})();