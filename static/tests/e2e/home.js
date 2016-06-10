describe('Main page test', function () {
    beforeEach(function () {
        browser.get('/#!/');
    });


    it('should load the homepage', function () {
        expect(browser.getTitle()).toBe('Prized.tv');
    });

});


