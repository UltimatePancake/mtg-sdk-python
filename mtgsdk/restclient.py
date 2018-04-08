#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of mtgsdk.
# https://github.com/MagicTheGathering/mtg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

import aiohttp
import traceback
from urllib.parse import urlencode


class RestClient:
    @staticmethod
    async def get(url, params={}):
        """Invoke an HTTP GET request on a url
        
        Args:
            url (string): URL endpoint to request
            params (dict): Dictionary of url parameters 
        Returns:
            dict: JSON response as a dictionary
        """
        request_url = url
        
        if len(params) > 0:
            request_url = "{}?{}".format(url, urlencode(params))

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(request_url, headers={'User-Agent': 'Mozilla/5.0'}) as response:
                    result = await response.json()

            return result
        except:
            traceback.print_exc()
            raise MtgException('Error retrieving data.')


class MtgException(Exception):
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description
