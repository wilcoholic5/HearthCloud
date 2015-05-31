
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope) {
    $scope.conn = new WebSocket('ws://localhost:1337');

    $scope.conn.onopen = (function (event) {
        console.log('connected')
    });

    $scope.conn.onmessage = (function (data) {
        console.log(data.data)
        var cardBlock = JSON.parse(data.data);

        //$scope.name = cardBlock.cardName;
        //$scope.image = cardBlock.img;
        //$scope.comments = cardBlock.comments;
        $scope.$apply(function(){
            $scope.result = cardBlock;
        });
        console.log(cardBlock)
    });

    $scope.firstName = "John";
    $scope.lastName = "Doe";

    $scope.findCard = (function () {
        console.log($scope.name)
        $scope.conn.send($scope.name);
    });
});