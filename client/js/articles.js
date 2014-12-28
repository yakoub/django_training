var Articles = angular.module('Articles', ['ngRoute']);

<<<<<<< HEAD
function router($routeProvider) {
  route = {
    templateUrl: function(params){
      return '/content/partials/articles/slider/' + params.pk;
    },
  };
  $routeProvider.when('/content/slider/:pk', route);
  
  route = {
    templateUrl: function(params){
      return '/content/partials/articles/scroller/' + params.pk;
    },
  };
  $routeProvider.when('/content/scroller/:pk', route);
=======
Articles.router = function($routeProvider) {

  route = {
    templateUrl: function(params){
      return '/django1/content/partials/articles/' + params.pk;
    },
  };
  $routeProvider.when('/content/:pk', route);
>>>>>>> d4db09aeda1fec8f13308eadee490b2cb95f8c17
 
  //$routeProvider.otherwise({redirectTo: '/content'});
}

<<<<<<< HEAD
Articles.config(['$routeProvider', router]);
=======
Articles.config(['$routeProvider', Articles.router]);
>>>>>>> d4db09aeda1fec8f13308eadee490b2cb95f8c17

Articles.controller('Scroller', function($scope) {
  $scope.type = 'Scroller'; 
});

Articles.controller('Slider', function($scope) {
  $scope.type = 'Slider'; 
});
