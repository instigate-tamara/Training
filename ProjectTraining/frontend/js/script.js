app.controller('show', function($scope, $http) {
	var sendRequest = function(url) {
		$scope.logs=['g1','g2','g3'];
		/*$http.jsonp(url).success(function(logs) {
			console.log(logs);
			$scope.logs = logs;
		});*/
	}
	sendRequest("http://localhost:8000/training?callback=JSON_CALLBACK")

	$scope.menuclick = function(p) {
        $scope.active =p+".html";
	}
});
