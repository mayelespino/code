/*eslint complexity: 0*/
'use strict';

var hasProperty = Object.prototype.hasOwnProperty;

/**
 * @class Obus
 * */
function Obus() {}

Obus.prototype = {

    /**
     * @public
     * @memberOf {Obus}
     * @method
     *
     * @constructs
     * */
    constructor: Obus,

    /**
     * @public
     * @memberOf {Obus}
     * @method
     *
     * @param {String} path
     *
     * @returns {Boolean}
     * */
    del: function (path) {
        var i;
        var k;
        var l;
        var parts = Obus.parse(path);
        var self = this;

        if (!parts.length) {
            return false;
        }

        for (i = 0, l = parts.length - 1; i < l; i += 1) {
            k = parts[i];

            if (self && hasProperty.call(self, k) && self[k] &&
                (typeof self[k] === 'object' || typeof self[k] === 'function')) {
                self = self[k];

                continue;
            }

            return false;
        }

        return delete self[parts[l]];
    },

    /**
     * @public
     * @memberOf {Obus}
     * @method
     *
     * @param {String} path
     * @param {*} data
     *
     * @returns {*}
     * */
    add: function (path, data) {
        var i;
        var k;
        var l;
        var parts = Obus.parse(path);
        var self = this;

        if (!parts.length) {
            for (i in data) {
                if (hasProperty.call(data, i)) {
                    self[i] = data[i];
                }
            }

            return self;
        }

        for (i = 0, l = parts.length - 1; i < l; i += 1) {
            k = parts[i];

            if (self && hasProperty.call(self, k) && self[k] &&
                (typeof self[k] === 'object' || typeof self[k] === 'function')) {
                self = self[k];

                continue;
            }

            self = self[k] = {};
        }

        k = parts[l];

        if (hasProperty.call(self, k) && self[k] &&
            (typeof self[k] === 'object' || typeof self[k] === 'function')) {
            self = self[k];
            for (i in data) {
                if (hasProperty.call(data, i)) {
                    self[i] = data[i];
                }
            }

            return self;
        }

        self[k] = data;

        return self[k];
    },

    /**
     * @public
     * @memberOf {Obus}
     * @method
     *
     * @param {String} path
     * @param {*} [def]
     *
     * @returns {*}
     * */
    get: function (path, def) {
        var i;
        var k;
        var l;
        var parts = Obus.parse(path);
        var self = this;

        for (i = 0, l = parts.length; i < l; i += 1) {
            k = parts[i];

            if (self && (typeof self === 'object' || typeof self === 'function') && hasProperty.call(self, k)) {
                self = self[k];

                continue;
            }

            return def;
        }

        if (self === void 0) {

            return def;
        }

        return self;
    },

    /**
     * @public
     * @memberOf {Obus}
     * @method
     *
     * @param {String} path
     *
     * @returns {Boolean}
     * */
    has: function (path) {
        var i;
        var k;
        var l;
        var parts = Obus.parse(path);
        var self = this;

        for (i = 0, l = parts.length; i < l; i += 1) {
            k = parts[i];

            if (self && (typeof self === 'object' || typeof self === 'function') && hasProperty.call(self, k)) {
                self = self[k];

                continue;
            }

            return false;
        }

        return true;
    },

    /**
     * @public
     * @memberOf {Obus}
     * @method
     *
     * @param {String} path
     * @param {*} data
     *
     * @returns {*}
     * */
    set: function (path, data) {
        var i;
        var k;
        var l;
        var parts = Obus.parse(path);
        var self = this;

        if (!parts.length) {
            for (i in self) {
                if (hasProperty.call(self, i)) {
                    delete self[i];
                }
            }

            for (i in data) {
                if (hasProperty.call(data, i)) {
                    self[i] = data[i];
                }
            }

            return self;
        }

        for (i = 0, l = parts.length - 1; i < l; i += 1) {
            k = parts[i];

            if (self && hasProperty.call(self, k) && self[k] &&
                (typeof self[k] === 'object' || typeof self[k] === 'function')) {
                self = self[k];

                continue;
            }

            self = self[k] = {};
        }

        k = parts[l];
        self[k] = data;

        return self[k];
    }
};

Obus.cache = {};

/**
 * @public
 * @static
 * @memberOf {Obus}
 * @method
 *
 * @param {String} path
 *
 * @returns {Array}
 * */
Obus.parse = function (path) {
    var parts = [];

    if (typeof path === 'string') {
        if (!hasProperty.call(Obus.cache, path)) {
            Obus.cache[path] = parse(path);
        }

        parts = Obus.cache[path];
    }

    return parts;
};

/**
 * @public
 * @static
 * @memberOf {Obus}
 * @method
 *
 * @param {Object} self
 * @param {String} path
 * @param {*} [def]
 *
 * @returns {*}
 * */
Obus.get = function (self, path, def) {
    return Obus.prototype.get.call(self, path, def);
};

/**
 * @public
 * @static
 * @memberOf {Obus}
 * @method
 *
 * @param {Object} self
 * @param {String} path
 * @param {*} data
 *
 * @returns {*}
 * */
Obus.set = function (self, path, data) {
    return Obus.prototype.set.call(self, path, data);
};

/**
 * @public
 * @static
 * @memberOf {Obus}
 * @method
 *
 * @param {Object} self
 * @param {String} path
 * @param {*} data
 *
 * @returns {*}
 * */
Obus.add = function (self, path, data) {
    return Obus.prototype.add.call(self, path, data);
};

/**
 * @public
 * @static
 * @memberOf {Obus}
 * @method
 *
 * @param {Object} self
 * @param {String} path
 *
 * @returns {Boolean}
 * */
Obus.has = function (self, path) {
    return Obus.prototype.has.call(self, path);
};

/**
 * @public
 * @static
 * @memberOf {Obus}
 * @method
 *
 * @param {Object} self
 * @param {String} path
 *
 * @returns {Boolean}
 * */
Obus.del = function (self, path) {
    return Obus.prototype.del.call(self, path);
};

var R_SEARCH = /^\s*([^\s])([\s\S]*)/;
var R_DEGRADE = /^\s*[^\s.\[]/;
var R_IDENT = /^\s*([_a-z$][\w$]*)([\s\S]*)$/i;
var R_OPEN_ACCESS = /^\s*(?:(\d+)|(['"]))([\s\S]*)$/;
var R_STRING1 = /^([^"]*)"([\s\S]*)$/;
var R_STRING2 = /^([^']*)'([\s\S]*)$/;
var R_CLOSE_ACCESS = /^\s*]([\s\S]*)$/;

function parse(s) {
    /*eslint  default-case: 0, complexity: 0*/
    var orig = s;
    var m;
    var state = '?';
    var parts = [];

    if (R_DEGRADE.test(s)) {
        state = '.';
    }

    while (state !== 'EOF') {

        switch (state) {

            case '?':
                m = R_SEARCH.exec(s);

                if (!m) {
                    state = 'EOF';
                    break;
                }

                s = m[2];
                state = m[1];
                break;

            case '.':
                m = R_IDENT.exec(s);

                if (!m) {
                    state = 'INVALID';
                    break;
                }

                s = m[2];
                parts[parts.length] = m[1];
                state = '?';
                break;

            case '[':
                m = R_OPEN_ACCESS.exec(s);

                if (!m) {
                    state = 'INVALID';
                    break;
                }

                s = m[3];

                if (m[1]) {
                    parts[parts.length] = parseInt(m[1], 10);
                    state = ']';
                    break;
                }

                state = m[2];
                break;

            case '"':
                m = R_STRING1.exec(s);

                if (!m) {
                    state = 'INVALID';
                    break;
                }

                s = m[2];
                parts[parts.length] = m[1];
                state = ']';
                break;

            case '\'':
                m = R_STRING2.exec(s);

                if (!m) {
                    state = 'INVALID';
                    break;
                }

                s = m[2];
                parts[parts.length] = m[1];
                state = ']';
                break;

            case ']':
                m = R_CLOSE_ACCESS.exec(s);

                if (!m) {
                    state = 'INVALID';
                    break;
                }

                s = m[1];
                state = '?';
                break;

            default:
                throw new SyntaxError(orig + '\n' + new Array(orig.length - s.length + 17).join(' ') + '^');

        }
    }

    return parts;
}

module.exports = Obus;
