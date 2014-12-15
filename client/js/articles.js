var Articles = angular.module('Articles', ['ngRoute']);

function router_test($routeProvider) {
  route = {
    templateUrl: '/django-static-1/js/articles.js',
  };
  $routeProvider.when('content/test', route);
}

function router($routeProvider) {
  route = {
    templateUrl: function(params){
      return '/django1/content/partials/articles/slider/' + params.pk;
    },
  };
  $routeProvider.when('content/slider/:pk', route);
  
  route = {
    templateUrl: function(params){
    console.log('run');
    console.log(params);
      return '/django1/content/partials/articles/scroller/' + params.pk;
    },
  };
  $routeProvider.when('content/scroller/:pk', route);
 
  //$routeProvider.otherwise({redirectTo: '/content'});
}

Articles.config(['$routeProvider', router_test]);

Articles.controller('first', function($scope) {
  $scope.list = [1,2,3,4,5]; 
});

