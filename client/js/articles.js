var Articles = angular.module('Articles', ['ngRoute']);

function router($routeProvider) {

  route = {
    templateUrl: function(params){
      return '/django1/content/partials/articles/' + params.pk;
    },
  };
  $routeProvider.when('/content/:pk', route);
 
  //$routeProvider.otherwise({redirectTo: '/content'});
}

Articles.config(['$routeProvider', router]);

Articles.controller('Scroller', function($scope) {
  $scope.type = 'Scroller'; 
});

Articles.controller('Slider', function($scope) {
  $scope.type = 'Slider'; 
});
