describe('Product detail test', function () {
    beforeEach(function () {
        browser.get('/#!/prize/6/');
    });

    it('should load product page', function () {

        var header = element(by.tagName('h2'));

        expect(header.getText()).toBe('VINTAGE FAUX FUR VEST');
    });

});


