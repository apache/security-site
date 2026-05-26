# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License. 

import asfquart
import dataclasses
from typing import Self

@dataclasses.dataclass(frozen=True)
class UserSession:
    client_session: asfquart.session.ClientSession | None

    @property
    def is_authenticated(self) -> bool:
        return self.client_session is not None

    @property
    def uid(self) -> str | None:
        return self.client_session.uid if self.client_session else None

    @property
    def fullname(self) -> str | None:
        return self.client_session.fullname if self.client_session else None

    @property
    def pmcs(self) -> list[str]:
        return self.client_session.committees if self.client_session else []

    @property
    def projects(self) -> list[str]:
        return self.client_session.projects if self.client_session else []

    @property
    def is_root(self) -> bool:
        return bool(self.client_session and self.client_session.isRoot)

    @classmethod
    async def create(cls) -> Self:
        try:
            client_session = await asfquart.session.read()
            return cls(client_session)
        except ASFQuartException as ex:
            #TODO
            exit(1)
