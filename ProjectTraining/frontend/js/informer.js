/*app.controller('informer', function($scope, $http) {

 var lecturerInformer = function (url){
 $scope.title='Lecturer';
 $scope.peoples =[];
 $http.jsonp(url).success(function(lecturers){
 console.log(lecturers);
 $scope.peoples = lecturers;

 });
 }

 var studentInformer = function (url){
 $scope.title='Student';
 /* $scope.peoples =[];
 $http.jsonp(url).success(function(students){
 console.log(students);
 $scope.peoples = students;
 });
 }

 $scope.informer= function(p){
 if (p==1) {
 lecturerInformer('http://localhost:8000/training/lecturer?callback=JSON_CALLBACK')
 }else{
 studentInformer('http://localhost:8000/training/student?callback=JSON_CALLBACK')
 };
 }

 });*/

app.controller('informer', function($scope, $http) {

	$scope.lecturerInformer = function() {
console.log('lecturers');
		$scope.title = 'Lecturer';
	/*	$scope.peoples = [];
		$http.jsonp('http://localhost:8000/training/lecturer?callback=JSON_CALLBACK').success(function(lecturers) {
			console.log(lecturers);
			$scope.peoples = lecturers;

		});*/
	}


	$scope.studentInformer = function() {
console.log('stud');
		$scope.title = 'Student';
	/*	$scope.peoples = [];
		$http.jsonp('http://localhost:8000/training/student?callback=JSON_CALLBACK').success(function(students) {
			console.log(students);
			$scope.peoples = students;
		});*/
	}
});
