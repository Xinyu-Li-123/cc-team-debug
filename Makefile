parse_log: error_log.txt
	./parse_log.sh error_log.txt error_args.txt

send_request_ref: send_request.py error_args.txt
	./send_request.py --args error_args.txt --type ref

send_request_our: send_request.py error_args.txt
	./send_request.py --args error_args.txt --type our
