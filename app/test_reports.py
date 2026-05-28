from app.reports import _asf_member_link


def test_asf_member_link_non_apache_to_uses_security_apache_org():
    email = {
        'to': 'Disclosure <disclosure@aisle.com>',
        'message_id': '<7200416e-bd53-4026-a0a1-f3cf4c00de86n@aisle.com>',
    }
    assert _asf_member_link(email) == (
        'https://lists.apache.org/thread/'
        '<7200416e-bd53-4026-a0a1-f3cf4c00de86n%40aisle.com>'
        '?<security.apache.org>'
    )


def test_asf_member_link_apache_to_uses_to_domain():
    email = {
        'to': 'security@cassandra.apache.org',
        'message_id': '<abc123@cassandra.apache.org>',
    }
    assert _asf_member_link(email) == (
        'https://lists.apache.org/thread/'
        '<abc123%40cassandra.apache.org>'
        '?<security.cassandra.apache.org>'
    )
