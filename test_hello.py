from hello import bye, hello


def test_hello():
	assert hello('nigga') == 'hello nigga'

def test_hello_mia():
	assert hello('mia') == 'hello mia'

def test_bye():
	assert bye('nigga') == 'bye nigga'

def test_bye_mia():
	assert bye('mia') == 'bye mia'
