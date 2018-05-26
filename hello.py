def application(environ, start_response):
    qs=environ.get('QUERY_STRING')
    qs=qs.split('&')
    resp=''
    for k in qs:
    	resp=resp+'\n'+k
    resp=resp+'\n'
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [resp.encode('utf-8')]
