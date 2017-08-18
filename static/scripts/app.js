var app = angular.module('funApp', []);

app.controller('funCtrl',['$scope', '$http', function($scope, $http) {

	//Function to search username
 	$scope.searchUsername = function() {
  $scope.message = "hello";
 		console.log("Hello");
    	var request = $http({
        	method:"GET",
        	url: "https://xkcd.com/1500/info.0.json",
      	});
	    request.success(function(data){
	    	console.log(data);
	    	$scope.data = data;
    	});
      	request.error(function(data){
        	console.log(data.message);
        	$scope.errorMessage = data.message;
      	});
    }
    $scope.searchUsername();
}]);