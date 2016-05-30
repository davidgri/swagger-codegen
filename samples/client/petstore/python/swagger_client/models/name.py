# coding: utf-8

"""
    Swagger Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\ 

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Name(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Name - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'int',
            'snake_case': 'int',
            '_property': 'str',
            '_123_number': 'int'
        }

        self.attribute_map = {
            'name': 'name',
            'snake_case': 'snake_case',
            '_property': 'property',
            '_123_number': '123Number'
        }

        self._name = None
        self._snake_case = None
        self.__property = None
        self.__123_number = None

    @property
    def name(self):
        """
        Gets the name of this Name.


        :return: The name of this Name.
        :rtype: int
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Name.


        :param name: The name of this Name.
        :type: int
        """
        
        self._name = name

    @property
    def snake_case(self):
        """
        Gets the snake_case of this Name.


        :return: The snake_case of this Name.
        :rtype: int
        """
        return self._snake_case

    @snake_case.setter
    def snake_case(self, snake_case):
        """
        Sets the snake_case of this Name.


        :param snake_case: The snake_case of this Name.
        :type: int
        """
        
        self._snake_case = snake_case

    @property
    def _property(self):
        """
        Gets the _property of this Name.


        :return: The _property of this Name.
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """
        Sets the _property of this Name.


        :param _property: The _property of this Name.
        :type: str
        """
        
        self.__property = _property

    @property
    def _123_number(self):
        """
        Gets the _123_number of this Name.


        :return: The _123_number of this Name.
        :rtype: int
        """
        return self.__123_number

    @_123_number.setter
    def _123_number(self, _123_number):
        """
        Sets the _123_number of this Name.


        :param _123_number: The _123_number of this Name.
        :type: int
        """
        
        self.__123_number = _123_number

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

