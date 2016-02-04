#!/usr/bin/perl

use Test::More;
# More informations: http://perldoc.perl.org/5.8.8/Test/More.html

######## Pre configuration ########
setup_env();

######## Tests ####################
note('test 1');
subtest 'test 1' => sub
{
    plan skip_all => 'skip';

    ok(1) or diag('Function return:', explain $hash);

    done_testing();
};


######## cleaning ########
clean_env();

done_testing();

sub setup_env()
{

}

sub clean_env()
{

}
