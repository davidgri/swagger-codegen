(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'));
  } else {
    // Browser globals (root is window)
    if (!root.SwaggerPetstore) {
      root.SwaggerPetstore = {};
    }
    root.SwaggerPetstore.EnumTest = factory(root.SwaggerPetstore.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';

  /**
   * The EnumTest model module.
   * @module model/EnumTest
   * @version 1.0.0
   */

  /**
   * Constructs a new <code>EnumTest</code>.
   * @alias module:model/EnumTest
   * @class
   */
  var exports = function() {
    var _this = this;




  };

  /**
   * Constructs a <code>EnumTest</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/EnumTest} obj Optional instance to populate.
   * @return {module:model/EnumTest} The populated <code>EnumTest</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('enum_string')) {
        obj['enum_string'] = ApiClient.convertToType(data['enum_string'], 'String');
      }
      if (data.hasOwnProperty('enum_integer')) {
        obj['enum_integer'] = ApiClient.convertToType(data['enum_integer'], 'Integer');
      }
      if (data.hasOwnProperty('enum_number')) {
        obj['enum_number'] = ApiClient.convertToType(data['enum_number'], 'Number');
      }
    }
    return obj;
  }


  /**
   * @member {module:model/EnumTest.EnumStringEnum} enum_string
   */
  exports.prototype['enum_string'] = undefined;

  /**
   * @member {module:model/EnumTest.EnumIntegerEnum} enum_integer
   */
  exports.prototype['enum_integer'] = undefined;

  /**
   * @member {module:model/EnumTest.EnumNumberEnum} enum_number
   */
  exports.prototype['enum_number'] = undefined;


  /**
   * Allowed values for the <code>enum_string</code> property.
   * @enum {String}
   * @readonly
   */
  exports.EnumStringEnum = {
    /**
     * value: "UPPER"
     * @const
     */
    "UPPER": "UPPER",
    /**
     * value: "lower"
     * @const
     */
    "lower": "lower"  };
  /**
   * Allowed values for the <code>enum_integer</code> property.
   * @enum {Integer}
   * @readonly
   */
  exports.EnumIntegerEnum = {
    /**
     * value: 1
     * @const
     */
    "1": 1,
    /**
     * value: -1
     * @const
     */
    "-1": -1  };
  /**
   * Allowed values for the <code>enum_number</code> property.
   * @enum {Number}
   * @readonly
   */
  exports.EnumNumberEnum = {
    /**
     * value: 1.1
     * @const
     */
    "1.1": 1.1,
    /**
     * value: -1.2
     * @const
     */
    "-1.2": -1.2  };


  return exports;
}));
