from common import info


def main():
    """
    Provides information about the database maintenance scripts.
    """
    info('')
    info('Hello, this is the database maintenance script runner')
    info('It will call the orcidlink service to perform maintenance tasks.')
    info('It requires the following environment variables:')
    info('')
    info('KBASE_ENDPOINT')
    info('  Indicates the base URL for the target deployment environment')
    info('  E.g. https://ci.kbase.us/services/')
    info('  Note that traditionally this setting has a terminal forward slash "/".')
    info("  The script doesn't care if it is present or not -- it will strip it off if it is found")
    info('')
    info('KBASE_AUTH_TOKEN')
    info('  The token for an account with orcidlink management privilege.')
    info('  This is an account with the custom role "orcidlink_manager".')
    info('')

if __name__ == '__main__':
    main()
