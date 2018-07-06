var mainapp = angular.module('mainapp', ['ngRoute']);

(function () {
    "use strict";
    angular.module("mainapp").controller("mainController", mainController);
    mainController.$inject = ["$scope", "$http"];

    function mainController($scope, $http) {
        var ctrl = this;
        ctrl.message = 'hellos antosh';
        ctrl.init = init;

        function init() {}
    }
})();