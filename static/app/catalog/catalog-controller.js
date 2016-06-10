/**
 * Products catalog controller
 * Categories loading, show product list
 */
(function () {
    'use strict';

    angular
        .module('mainApp')
        .controller('CatalogController', CatalogController);

    CatalogController.$inject = ['$scope', '$timeout', 'CatalogService', 'CompetitionService', 'PrizeService'];

    function CatalogController($scope, $timeout, CatalogService, CompetitionService) {
        var vm = this;
        vm.categories = CatalogService.getCategories();
        vm.products = [];
        vm.selectedProduct = {};
        vm.photoCount = 0;
        vm.selectedCategoryId = 0;
        vm.competition = CompetitionService.getCompetition();
        vm.prizes = CompetitionService.getPrizes();

        vm.showProducts = function (cid) {
            vm.selectedCategoryId = cid;
            return CatalogService.loadProducts(cid).then(function (products) {
                vm.products = products;
            });
        };
        
        vm.showChildProducts = function (cid) {
            vm.SelectedCategoryId = cid;
            return CatalogService.loadChildProducts(cid).then(function(products){
                vm.products = products;
            });
        };

        vm.showProduct = function (index) {
            $scope.$broadcast('productPopupOpen', vm.products[index].id);
        };

        function init() {
            vm.showProducts(0).then(function() {
                vm.products = vm.prizes.concat(vm.products);
            });



            $timeout(function () {
                // init Masonry
                var $grid = $('.grid').masonry({
                    itemSelector: '.grid-item',
                    percentPosition: true,
                    columnWidth: '.grid-sizer'
                });
                // layout Isotope after each image loads
                $grid.imagesLoaded().progress(function () {
                    $grid.masonry();
                });
            }, 1000);

        }



        init();
    }
})();
