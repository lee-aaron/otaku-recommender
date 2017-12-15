var api = function() {
    // run code here, or...
}; 

// ...add a method, which we do in this example:
api.prototype.getList = function() {
    return "testing!";
};

// now expose with module.exports:
exports.api = api;