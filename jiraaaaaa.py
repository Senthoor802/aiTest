import requests

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'apiKey': 'd12b80c0f85b2a2521b60d96c11a2b7c7f61d359f6cef35014c8789835c178cb7377cd6cb4f221f4a925b88754d2ab58c5b74f5b64e62a5caf4fafd3cba03220ba0ba84d2042dafc2013d2d2f090237f',
    'Authorization': 'ATATT3xFfGF0FKcYC1r9eSxZWL1naME9GeIw8Fas37gOAWZ9TwmHh9f3EJ7jNNUfr5An2xXxWlLnc9PSeXXVnvx8kBmcQcpnbpFvF955eMXBmLZW2-9DOKl2RB0EnflEI9RKAEaooS3ZmmUtaRf6TVT6poAwe_y6uW01hlXVY-jbfyl7Tz-3F9g=BEBC16F0'
}

# request = requests.Request('GET', 'https://americold.atlassian.net/rest/qtm4j/qapi/latest/projects/10524/filterModule?filterName=&startAt=&maxResults=', headers=headers)
# response = requests.get(request.url, headers=headers)
# print(response.text)

request = requests.Request('GET', 'https://americold.atlassian.net/rest/qtm4j/qapi/latest/testcases/zR4T9bpFqNJxa', headers=headers)
response = requests.get(request.url, headers=headers)
print(response.text)