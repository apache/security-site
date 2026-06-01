from app.reports import Reporter, _asf_member_link, _project_link, _reporter


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


def test_project_link_returns_first_apache_email():
    emails = [
        {'to': 'reporter@aisle.com', 'message_id': '<a@aisle.com>'},
        {'to': 'security@cassandra.apache.org', 'message_id': '<b@cassandra.apache.org>'},
        {'to': 'security@cassandra.apache.org', 'message_id': '<c@cassandra.apache.org>'},
    ]
    assert _project_link(emails) == (
        'https://lists.apache.org/thread/'
        '<b%40cassandra.apache.org>'
        '?<security.cassandra.apache.org>'
    )


def test_project_link_only_considers_first_five():
    emails = [{'to': 'reporter@aisle.com', 'message_id': f'<{i}@aisle.com>'} for i in range(5)]
    emails.append({'to': 'security@cassandra.apache.org', 'message_id': '<late@cassandra.apache.org>'})
    assert _project_link(emails) is None


def test_project_link_returns_none_when_no_apache_recipient():
    emails = [
        {'to': 'reporter@aisle.com', 'message_id': '<a@aisle.com>'},
        {'to': 'disclosure@vendor.example', 'message_id': '<b@vendor.example>'},
    ]
    assert _project_link(emails) is None


def test_asf_member_link_uses_cc_when_to_is_non_apache():
    email = {
        'to': 'reporter@aisle.com',
        'cc': 'security@cassandra.apache.org',
        'message_id': '<abc@aisle.com>',
    }
    assert _asf_member_link(email) == (
        'https://lists.apache.org/thread/'
        '<abc%40aisle.com>'
        '?<security.cassandra.apache.org>'
    )


def test_asf_member_link_prefers_to_over_cc():
    email = {
        'to': 'security@cassandra.apache.org',
        'cc': 'security@kafka.apache.org',
        'message_id': '<abc@cassandra.apache.org>',
    }
    assert _asf_member_link(email) == (
        'https://lists.apache.org/thread/'
        '<abc%40cassandra.apache.org>'
        '?<security.cassandra.apache.org>'
    )


def test_project_link_finds_apache_address_in_cc():
    emails = [
        {
            'to': 'reporter@aisle.com',
            'cc': 'security@cassandra.apache.org',
            'message_id': '<a@aisle.com>',
        },
    ]
    assert _project_link(emails) == (
        'https://lists.apache.org/thread/'
        '<a%40aisle.com>'
        '?<security.cassandra.apache.org>'
    )


def test_reporter_uses_from_when_not_via():
    email = {'from': 'Jane Q. Reporter <jane@aisle.com>'}
    assert _reporter(email) == Reporter(name='Jane Q. Reporter', email='jane@aisle.com')


def test_reporter_falls_back_to_reply_to_when_via_security_list():
    email = {
        'from': '\"Jane Reporter via Security\" <security@apache.org>',
        'reply_to': 'Jane Reporter <jane@aisle.com>',
    }
    assert _reporter(email) == Reporter(name='Jane Reporter', email='jane@aisle.com')


def test_reporter_falls_back_to_reply_to_when_via_project_list():
    email = {
        'from': 'Jane Reporter via Security <security@cassandra.apache.org>',
        'reply_to': 'Jane Reporter <jane@aisle.com>',
    }
    assert _reporter(email) == Reporter(name='Jane Reporter', email='jane@aisle.com')


def test_reporter_returns_none_when_via_apache_and_no_reply_to():
    email = {'from': 'Jane Reporter via Security <security@cassandra.apache.org>'}
    assert _reporter(email) is None


def test_reporter_returns_none_when_from_missing():
    assert _reporter({}) is None


def test_reporter_initials_from_name():
    assert Reporter(name='Jane Q. Reporter', email='jane@aisle.com').initials == 'JQR'


def test_reporter_initials_fall_back_to_email_local_part():
    assert Reporter(name='', email='alice@example.com').initials == 'A'
