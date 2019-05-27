<?php

namespace App\Provider;

use App\Foundation\Socialite\AmazonProvider;
use Illuminate\COntracts\Foundation\Application;
use Illuminate\Support\ServiceProvider;
use Laravel\Socialite\Contracts\Factory;
use Laravel\Socialite\SocialiteManager;

class SocialiteServiceProvider extends ServiceProvider
{
    /**
     * @param Factory|SocialiteManager $factory
     */
    public function boot(Factory $factory)
    {
        $factory->extend('amazon', function(Application $app) use($factory) {
            return $factory->buildProvider(
                AmazonProvider::class,
                $app['config']['services.amazon']
            );
        });
    }
}