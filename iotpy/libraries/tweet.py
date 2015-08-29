#!/usr/bin/python

def twythonConfiguration():
    configuration = ConfigParser.ConfigParser()
    configuration.read('configuration/credentials.config')
    consumer_key = configuration.get('twitter','consumer_key')
    consumer_secret = configuration.get('twitter','consumer_secret')
    access_token = configuration.get('twitter','access_token')
    access_token_secret = configuration.get('twitter','access_token_secret')
    twythonid = Twython(consumer_key,consumer_secret,access_token,access_token_secret)
    return twythonid

def twythonTimelineSet(twitterid, status, media):
    logging.info(status)
    if media:
        photo = open(media,'rb')
        twythonid.update_status_with_media(media=photo, status=status)
    else:
        twythonid.update_status(status=status)

# End of File
