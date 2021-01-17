# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

import json

import redis


class RedisController:
    def __init__(self, host: str, port: int):
        self._redis = redis.Redis(host=host, port=port, encoding="utf-8", decode_responses=True)

    """User Related."""

    def set_user_details(self, cluster_name: str, user_id: str, user_details: dict) -> None:
        return self._redis.hset(
            f"{cluster_name}:id_to_user_details",
            user_id,
            json.dumps(obj=user_details)
        )