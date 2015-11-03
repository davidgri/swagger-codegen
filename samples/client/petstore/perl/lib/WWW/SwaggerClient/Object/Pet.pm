package WWW::SwaggerClient::Object::Pet;

require 5.6.0;
use strict;
use warnings;
use utf8;
use JSON qw(decode_json);
use Data::Dumper;
use Module::Runtime qw(use_module);
use Log::Any qw($log);
use Date::Parse;
use DateTime;

use base "WWW::SwaggerClient::Object::BaseObject";

#
#
#
#NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
#

my $swagger_types = {
    'id' => 'int',
    'category' => 'Category',
    'name' => 'string',
    'photo_urls' => 'ARRAY[string]',
    'tags' => 'ARRAY[Tag]',
    'status' => 'string'
};

my $attribute_map = {
    'id' => 'id',
    'category' => 'category',
    'name' => 'name',
    'photo_urls' => 'photoUrls',
    'tags' => 'tags',
    'status' => 'status'
};

__PACKAGE__->mk_accessors(keys %$attribute_map);

# new object
sub new { 
    my ($class, %args) = @_; 
    my $self = { 
        #
        'id' => $args{'id'}, 
        #
        'category' => $args{'category'}, 
        #
        'name' => $args{'name'}, 
        #
        'photo_urls' => $args{'photoUrls'}, 
        #
        'tags' => $args{'tags'}, 
        #pet status in the store
        'status' => $args{'status'}
    }; 

    return bless $self, $class; 
}  

# get swagger type of the attribute
sub get_swagger_types {
    return $swagger_types;
}

# get attribute mappping
sub get_attribute_map {
    return $attribute_map;
}

1;
