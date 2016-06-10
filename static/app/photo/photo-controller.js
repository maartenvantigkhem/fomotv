/**
 * Controller for selecting photo from Facebook
 * @param $scope
 * @param $http
 * @param $timeout
 * @param ezfb
 * @param PhotoService
 * @param Auth
 * @constructor
 */
function FacebookSelectPhotoController($scope, $http, $timeout, $routeParams, ezfb, PhotoService, Auth, PhotoUploadFactory) {

    $scope.albums = PhotoService.getAlbums();
    $scope.photos = [];
    $scope.selectedAlbum = 0;
    $scope.selectedPhoto = null;
    $scope.showAlbums = true;
    $scope.competitionId = 0;

    $scope.showPhotoList = function(albumIndex){
        $scope.selectedAlbum = albumIndex;

        if($scope.albums[albumIndex] != 'undefined')
        {
            albumId = $scope.albums[albumIndex].id

            ezfb.api('/' + albumId + '/photos?fields=picture,source', function(res)
            {
                $scope.photos = res.data;
                console.log(res.data)
            });
        }

    };

    $scope.selectPhoto = function(index){
        $scope.selectedPhoto = $scope.photos[index];
        $scope.uploadPhoto();
    };

    $scope.uploadPhoto = function() {
        if($scope.selectedPhoto != null)
        {
            $scope.$parent.myImage = $scope.selectedPhoto.source;
            $scope.showCropImagePopup($scope.competitionId);
        }
        else {
            $scope.$parent.showInfoMessage("Please, select photo first");
        }

    };

    var init = function() {
        if (typeof $routeParams.competition_id != 'undefined') {
            $scope.competitionId = $routeParams.competition_id;
        }

        ezfb.getLoginStatus().then(function(res) {
            if(res.status !== "connected") {
                window.location = "#!/";
            }
            else {
                $scope.showPhotoList(0);
            }

        });

        //var uploader = PhotoUploadFactory.build('test');
        //console.log(uploader.getName());
    };

    (function() {  // init
        $timeout( function() {
            album_menu();
            $('.btn-alb-mob-filt').click(function(e) {
                $('body').toggleClass('mob-pdl200');
                $('.alb-list-mob').toggleClass('active');
                $('.mob-pdl200').css('width',Win_w);
                e.stopPropagation();
            });
        }, 10);
    })();

    init();
}

/**
 * Selecting photo from Instagram
 *
 * @param $scope
 * @param $http
 * @param Auth
 * @constructor
 */
function InstagramSelectPhotoController($scope, $http, $routeParams, Auth) {
    $scope.photos = [];
    $scope.selectedPhoto = null;
    $scope.showAlbums = false;
    $scope.competitionId = 0;

    $scope.showPhotoList = function() {

        $http.jsonp('https://api.instagram.com/v1/users/'+ Auth.getSocialUserId()
                +'/media/recent/?access_token=' + Auth.getAccessToken() + '&callback=JSON_CALLBACK').then(
            function(res) {
                res.data.data.forEach(function(current) {
                    $scope.photos.push({
                        picture: current.images.thumbnail.url,
                        id: current.id,
                        source: current.images.standard_resolution.url
                    })
                });

            },
            function(error) {
                console.log(error);
            }

        );

    };

    $scope.selectPhoto = function(index){
        if($scope.selectedPhoto != null && $scope.selectedPhoto.id == $scope.photos[index].id){
            $scope.selectedPhoto = null;
        }
        else{
            $scope.selectedPhoto = $scope.photos[index];
        }
        $scope.uploadPhoto();
    };

    $scope.uploadPhoto = function(){
        if($scope.selectedPhoto != null)
        {
            $('#spinner-mod').modal('show');
            $http({
                method: 'POST',
                url: '/upload_photo_by_url/',
                data: $.param(
                    {
                        'photo_url': $scope.selectedPhoto.source,
                        'competition_id': $scope.competitionId
                    }),
                headers: {'Content-Type': 'application/x-www-form-urlencoded'}
            }).
              success(function(data, status, headers, config) {
                // this callback will be called asynchronously
                // when the response is available
                    //console.log(data.photo_id)
                    $('#spinner-mod').modal('hide');
                    window.location = "#!/competition/" + data.competition_id + "/photo/" + data.photo_id
              }).
              error(function(data, status, headers, config) {
                // called asynchronously if an error occurs
                // or server returns response with an error status.
                    //alert('error: ' + status);
                    $('#spinner-mod').modal('hide');
                    $scope.$parent.showInfoMessage("Error while photo upload, try again");
                    //console.log("Error photo upload");
              });
        }
    };

    var init = function() {
        if (typeof $routeParams.competition_id != 'undefined') {
            $scope.competitionId = $routeParams.competition_id;
        }

        if(Auth.getAccessToken() == "")
        {
            Auth.loadAccessToken().then(function() {
                $scope.showPhotoList();
            })
        }
        else {
            $scope.showPhotoList();
        }
    };

    init();
}

angular.module('mainApp')
.controller('FacebookSelectPhotoController',
        ['$scope', '$http', '$timeout', '$routeParams', 'ezfb', 'PhotoService', 'Auth', 'PhotoUploadFactory',
            FacebookSelectPhotoController])
.controller('InstagramSelectPhotoController',
        ['$scope', '$http', '$routeParams', 'Auth', InstagramSelectPhotoController]);
