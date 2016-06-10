/*
 exports.config = {
 seleniumAddress: 'http://localhost:7000/',
 directConnect: true,
 specs: ['./**.js']
 };




 */

// Karma configuration
module.exports = function (config) {
    config.set({
        // base path, that will be used to resolve files and exclude
        basePath: '..',

        // testing framework to use (jasmine/mocha/qunit/...)
        //frameworks: ['ng-scenario', 'jasmine'],
        frameworks: ['jasmine'],

        // list of files / patterns to load in the browser
        files: [
            'bower_components/angular/angular.js',
            'bower_components/angular-route/angular-route.js',
            'bower_components/angular-mocks/angular-mocks.js',
            'bower_components/**/*.min.js',
            'js/jquery.js',
            'js/modernizr.custom.js',
            'js/*.js',
            'app/main-app.js',
            'app/**/*.js',
            'tests/competition/*.js',
            'tests/e2e/*.js'
        ],

        // list of files / patterns to exclude
        exclude: [
            'js/admin.js',
            'js/jquery.joyride-2.1.js',
            'js/npm.js'
        ],

        // web server port
        port: 8080,

        // level of logging
        // possible values: LOG_DISABLE || LOG_ERROR || LOG_WARN || LOG_INFO || LOG_DEBUG
        logLevel: config.LOG_INFO,

        // enable / disable watching file and executing tests whenever any file changes
        autoWatch: false,

        // Start these browsers, currently available:
        // - Chrome
        // - ChromeCanary
        // - Firefox
        // - Opera
        // - Safari (only Mac)
        // - PhantomJS
        // - IE (only Windows)
        browsers: ['Chrome'],

        // coverage reporter generates the coverage
        reporters: ['progress', 'coverage'],

        preprocessors: {
          // source files, that you wanna generate coverage for
          // do not include tests or libraries
          // (these files will be instrumented by Istanbul)
          'app/**/*.js' : ['coverage']
        },

        // optionally, configure the reporter
        coverageReporter: {
          type : 'html',
          dir : 'tests/coverage/'
        },

        // Continuous Integration mode
        // if true, it capture browsers, run tests and exit
        singleRun: false
    });
};