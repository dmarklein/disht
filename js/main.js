/**
 * Main AngularJS Web Application
 */
var app = angular.module('disht', [
  'ngRoute'
]);

/**
 * Configure the Routes
 */
app.config(['$routeProvider', function ($routeProvider) {
  $routeProvider
    // Home
    .when("/", {templateUrl: "partials/home.html", controller: "DishController"})
    .when("/home", {templateUrl: "partials/home.html", controller: "DishController"})
    // Pages
    .when("/add", {templateUrl: "partials/new_dish.html", controller: "DishController"})
    .when("/search", {templateUrl: "partials/listing.html", controller: "SearchController"})
    // else 404
    .otherwise("/404", {templateUrl: "partials/404.html", controller: "DishController"});
}]);

/**
 * Controls the Blog
 */
app.controller('DishController', function (/* $scope, $location, $http */) {
  console.log("Dish Controller reporting for duty.");

});

/**
 * Controls all other Pages
 */
app.controller('SearchController', function (/* $scope, $location, $http */) {
  console.log("Search Controller reporting for duty.");

});

$(document).ready(function ()
{
  $("#submitSearch").click(function () {console.log("search button clicked")});

})
