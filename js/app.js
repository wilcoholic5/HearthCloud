
var app = angular.module('myApp', ['ngSanitize']);
app.controller('myCtrl', function($scope) {
    $scope.conn = new WebSocket('ws://localhost:1337');

    $scope.conn.onopen = (function (event) {
        console.log('connected')
    });

    $scope.showContent = function($fileContent){
        console.log('running')
        $scope.content = $fileContent;
    };

    $scope.conn.onmessage = (function (data) {
        console.log(data.data)
        var cardBlock = JSON.parse(data.data);

        //$scope.name = cardBlock.cardName;
        //$scope.image = cardBlock.img;
        //$scope.comments = cardBlock.comments;
        $scope.$apply(function(){
            $scope.result = cardBlock;
            var words = [];
            //cardBlock.comments.forEach(function (entry) {
            //    console.log(entry[1])
            //    for (var i = 0; i < entry[1]; i++) {
            //        console.log('push ' + entry[0])
            //        words.push(entry[0])
            //    }
            //});
            update($scope.result.comments)

            $scope.result.fileLoc = "../cards/Polarity/" + $scope.result.cardName + ".txt";
            $scope.readFile($scope.result.fileLoc);
            $scope.result.comments = words;

        });
        console.log(cardBlock)
    });

    $scope.clean = (function (html) {
        return function(html){
            return $scope.trustAsHtml(html);
        }
    })

    $scope.findCard = (function () {
        console.log($scope.name)
        $scope.conn.send($scope.name);
    });


    $scope.readFile = (function(fileLoc) {
        $.get( fileLoc, function( data ) {
            $( "body" )
                .append( "Name: " ) // John
                .append( "Time: "); //  2pm
        }, "json" );
    });
});

function draw(words) {
    console.log("words here")
    console.log(words)
    d3.select(".wrapper").append("svg")
        .attr("width", 1000)
        .attr("height", 1000)
        .append("g")
        .attr("transform", "translate(600,600)")
        .selectAll("text")
        .data(words)
        .enter().append("text")
        .style("font-size", function(d) { return d.size + "px"; })
        .style("font-family", "Impact")
        .style("border", "1px solid black")
        .style("fill", function(d, i) { return fill(i); })
        .attr("text-anchor", "middle")
        .attr("transform", function(d) {
            return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
        })
        .text(function(d) { return d.text; });
}