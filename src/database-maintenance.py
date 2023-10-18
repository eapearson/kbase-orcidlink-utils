import os
import sys

from common import error, info, json_rpc, success


def load_and_check_environemt_variables():
    kbase_auth_token = os.environ.get('KBASE_AUTH_TOKEN')
    if kbase_auth_token is None:
        error('The KBASE_AUTH_TOKEN environment variable must be provided')
        error('Run the "help.py" script for more information')
        sys.exit(1)

    service_base_url = os.environ.get('KBASE_ENDPOINT')
    if service_base_url is None:
        error('The KBASE_ENDPOINT environment variable must be provided')
        error('Run the "help.py" script for more information')
        sys.exit(1)

    return kbase_auth_token, service_base_url


def get_service_info(url):
    return json_rpc(url, 'info')


def get_stats(url, kbase_auth_token):
    return json_rpc(url, 'get-stats', auth=kbase_auth_token)

def get_total_expired(url, auth):
    stats = get_stats(url, auth)
    return (
        stats["stats"]["linking_sessions_initial"]["expired"] +
        stats["stats"]["linking_sessions_started"]["expired"] +
        stats["stats"]["linking_sessions_completed"]["expired"]
    )

def delete_expired_linking_sessions(url, kbase_auth_token):
    return json_rpc(url, 'delete-expired-linking-sessions', auth=kbase_auth_token)


def main():
    """
    Calls the orcidlink service method "delete-expired-linking-sessions"
    """
    info('Loading and checking environment variables...')

    kbase_auth_token, service_base_url = load_and_check_environemt_variables()

    info('KBASE_AUTH_TOKEN is present')
    info(f'KBASE_ENDPOINT is "{service_base_url}"')

    success('Environment variables look fine')

    if service_base_url.endswith('/'):
        service_base_url = service_base_url[:-1]

    orcidlink_url = os.path.join(service_base_url, "orcidlink/api/v1")

    # Ping to be sure orcidlink service is running, and to document the version
    orcidlink_info = get_service_info(orcidlink_url)
    success('Successfully contacted orcidlink service')
    info(f'Service version is {orcidlink_info["service-description"]["version"]}')

    # See if there are any expired linking sessions
    total_expired = get_total_expired(orcidlink_url, kbase_auth_token)

    if total_expired == 0:
        success('No expired linking sessions found - no action will be taken')
        return

    info((
        f'{total_expired} expired linking session{"s" if total_expired != 1 else ""}'
        ' will be deleted'
    ))

    delete_expired_linking_sessions(orcidlink_url, kbase_auth_token)

    total_expired = get_total_expired(orcidlink_url, kbase_auth_token)

    if total_expired == 0:
        success('successfully deleted all expired linking sessions')
    else:
        error(f'deletion failed - there are still {total_expired} expired linking sessions')


if __name__ == '__main__':
    main()
