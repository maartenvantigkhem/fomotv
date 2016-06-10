"use strict";

describe("competition service", function () {
    var httpBackend, CompetitionService;

    beforeEach(function () {
        angular.mock.module("myConfig", function ($provide) {
            $provide.constant("appConfig", { facebookAppId: 0  });
        });

        angular.mock.module("mainApp", function () {
            // Something else
        });
    });

    beforeEach(inject(function ($injector, _CompetitionService_) {
        //competitionService = _competitionService_;
        httpBackend = $injector.get('$httpBackend');
        CompetitionService = _CompetitionService_;
    }));

    it("should return competition list", function () {
        httpBackend.when("GET", "/api/v1/competitions?active_flag=True&page_size=3").respond(
            {
                "results":
                [
                  {"name": ""}
                ]
            }
        );
        CompetitionService.getActiveList().then(function (list) {
            expect(list).toEqual([
                {"name": ""}
            ]);
        });
        httpBackend.flush();
    });
});