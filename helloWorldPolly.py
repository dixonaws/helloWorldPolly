import boto3
import os
import sys
import subprocess
from contextlib import closing
from tempfile import gettempdir

client=boto3.client('polly')

response = client.synthesize_speech(
    OutputFormat='mp3',
    SampleRate='8000',
    Text='Hello world',
    TextType='text',
    VoiceId='Joanna',
)

print(response)

with closing(response['AudioStream']) as stream:
	output='helloWorldPolly.mp3'

	try:
		with open(output, 'wb') as file:
			file.write(stream.read())
	except IOError as error:
		print(error)
		sys.exit(-1)










