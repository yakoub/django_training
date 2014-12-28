var Articles = angular.module('Articles', ['ngRoute']);

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
 
  //$routeProvider.otherwise({redirectTo: '/content'});
}

Articles.config(['$routeProvider', router]);

Articles.controller('first', function($scope) {
  $scope.list = [1,2,3,4,5]; 
});

