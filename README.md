This project extract mismatched requests from Sail's error log, and make these requests with Python to compare the raw response from reference server and our server.

First, you need to obtain the argumetns of mismatched requests, and save it to `error_args.txt`.

Next, you can run the following commands to get raw response from reference and our server, and save in two pickle files separately

```bash
make send_request_ref
make send_request_our
```
