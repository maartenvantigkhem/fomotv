/**
 * Catalog service
 */
(function () {
    'use strict';

    angular
        .module('mainApp')
        .factory('CatalogService', CatalogService);

    CatalogService.$inject = ['$http'];

    /**
     * @namespace Auth
     * @returns {Factory}
     */
    function CatalogService($http) {
        var categories = null;
        var products = null;

        var CatalogService = {
            loadCategories: loadCategories,
            loadProducts: loadProducts,
            loadChildProducts: loadChildProducts,
            loadProduct: loadProduct,
            getCategories: getCategories
        };

        function loadCategories() {
            return $http.get('/api/v1/categories/tree')
            .then(
                function (res) {
                    categories = res.data.tree;
                    //console.log(res.data);
                    return categories;

                },
                function (res) {
                    console.log('error categories list loading');
                }
            );
        }

        function loadProducts(cid) {
            return $http.get('/api/v1/categories/'+cid+'/products/')
            .then(
                function (res) {
                    products = res.data;
                    //console.log(res.data);
                    return products;
                },
                function (res) {
                    console.log('error products list loading');
                }
            );
        }
        
        function loadChildProducts(cid) {
            return $http.get('/api/v1/categories/'+cid+'/childproducts/')
            .then(
                function (res) {
                    products = res.data;
                    return products;
                },
                function (res) {
                    console.log('error products list loading');
                }
            );
        }

        function loadProduct(id) {
            return $http.get('/api/v1/prizes/' + id + '/')
            .then(
                function (res) {
                    return res.data;
                },
                function (res) {
                    console.log('error product loading');
                }
            );
        }

        function getCategories() {
            return categories;
        }

        return CatalogService;
    }
})();