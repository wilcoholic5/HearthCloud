
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
            cardBlock.comments.forEach(function (entry) {
                for (var i = 0; i < entry[1]; i++) {
                    words.push(entry[0])
                }
            });
            update(words)

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
    d3.select("body").append("svg")
        .attr("width", 300)
        .attr("height", 300)
        .append("g")
        .attr("transform", "translate(150,150)")
        .selectAll("text")
        .data(words)
        .enter().append("text")
        .style("font-size", function(d) { return d.size + "px"; })
        .style("font-family", "Impact")
        .style("fill", function(d, i) { return fill(i); })
        .attr("text-anchor", "middle")
        .attr("transform", function(d) {
            return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
        })
        .text(function(d) { return d.text; });
}