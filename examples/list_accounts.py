#!/usr/bin/env python

# Copyright (c) 2022 Exograd SAS.
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parents[1]))

from tabulate import tabulate

import eventline

client = eventline.APIClient()

table = []

cursor = eventline.Cursor(sort="name")
while cursor is not None:
    page = client.get_accounts(cursor=cursor)
    for account in page.elements:
        table.append([account.email_address, account.name])
    cursor = page.next

print(tabulate(table, ["Email address", "Name"]))
