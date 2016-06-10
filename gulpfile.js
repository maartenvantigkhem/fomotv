var gulp = require('gulp');
var Server = require('karma').Server;

var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var exec = require('child_process').exec;

gulp.task('scripts', function() {
  return gulp.src(['./static/app/*.js', './static/app/**/*.js'])
    .pipe(concat('app.min.js'))
    .pipe(gulp.dest('./static/dist/'));
});

gulp.task('uglify', function() {
    setTimeout( function(){
        gulp.src('static/dist/app.min.js')
            .pipe(uglify())
            .pipe(gulp.dest('static/dist'))
    } , 5000)
});

gulp.task('test', function (done) {
  new Server({
    configFile: __dirname + '/static/tests/karma.conf.js',
    singleRun: true
  }, done).start();
});

gulp.task('django', function (done) {
    var proc = exec('PYTHONUNBUFFERED=1 python ./manage.py runserver 8000');
});

var protractor = require("gulp-protractor").protractor;

gulp.task('e2e', function() {
    return gulp.src(["./static/tests/e2e/*.js"])
        .pipe(protractor({
            configFile:  __dirname + '/static/tests/protractor.conf.js',
            args: ['--baseUrl', 'http://127.0.0.1:8000']
        }))
        .on('error', function(e) { throw e })
});

// The default task (called when you run `gulp` from cli)
//gulp.task('default', ['scripts', 'uglify']);
gulp.task('default', ['scripts']);