app.controller('log', function($scope) {
	$scope.load = function() {

		$scope.subjects = [{
			id : '0',
			name : 'subject1',
	

		}, {
			id : '1',
			name : 'subject2',


		}, {
			id : '2',
			name : 'subject3',


		}, {
			id : '3',
			name : 'subject4',
		

		}]

		$scope.students = [{
			id : '0',
			name : 'kuku',
			surname : 'kukuyan'

		}, {
			id : '1',
			name : 'bubu',
			surname : 'bubuyan'

		}, {
			id : '2',
			name : 'gugu',
			surname : 'guguyan'

		}, {
			id : '3',
			name : 'fufu',
			surname : 'fufuyan'

		}]
	}
	$scope.rol = function(p) {
		if (p == '1') {
			$scope.roll = [{
				day : '05.01.14',
				student : [{
					id : '0',
					absence : true,
					mark : '1'
				}, {
					id : '1',
					absence : true,
					mark : '2'
				}, {
					id : '3',
					absence : true,
					mark : '3'
				}]

			}, {
				day : '06.01.14',
				student : [{
					id : '2',
					absence : false,
					mark : ''
				}, {
					id : '1',
					absence : true,
					mark : '5'
				}, {
					id : '3',
					absence : true,
					mark : '6'
				}]

			}]
		}
	}
});

/*
 $scope.data=[{
 student:[{
 name
 }]
 subject:[{
 name
 }]
 }]
 $scope.data1 = [{
 name : 'matematiks',
 student : [{
 name : 'kuku',
 day : [{
 day : '20.05.12',
 mark : 5,
 absence:false
 }
 ]

 }]
 }]
 */
