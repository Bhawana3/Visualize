angular
  .module('myApp', ['chart.js'])
.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');
}])
// controller here
  .controller('FirstCtrl', function($scope,$http) {

    $scope.options= {legend:{fullWidth:false,boxWidth:'350px'}};
    $scope.labels = ['positive','negative','neutral'];
    $scope.data = [];
    $scope.hotels=[];

    $http.get("/hotel")
      .then(function(response) {
        var hotelDatas = response.data.data;
        var positives = 0;
        var negatives = 0;
        var neutrals = 0;
        angular.forEach(hotelDatas,function(hotelData){
          var hotel = {};
          hotel.name = hotelData._id.unit;
          hotel.reviews = hotelData.reviews;
          hotel.chartData = [];
          hotel.chartData.push(hotelData.positive);
          hotel.chartData.push(hotelData.negative);
          hotel.chartData.push(hotelData.neutral);
          $scope.hotels.push(hotel);
          positives = positives + hotelData.positive ;
          negatives = negatives + hotelData.negative ;
          neutrals = neutrals + hotelData.neutral ;
        })

        var hotelChain = {};
        hotelChain.name = hotelDatas[0]._id.chain;
        hotelChain.chartData = [];
        hotelChain.chartData.push(positives);
        hotelChain.chartData.push(negatives);
        hotelChain.chartData.push(neutrals);
        $scope.hotels.unshift(hotelChain);

      });
  });