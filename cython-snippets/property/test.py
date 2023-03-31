import foo

ssl_params = foo.PySslParams()
ssl_params.port = 443
ssl_params.use_tls = True

client = foo.create_client(ssl_params)
client.send(b"Hello, world!")
client.close()

client = foo.PySockClient(ssl_params)
client.send(b"Hello, world!")
client.close()