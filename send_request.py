#!/usr/bin/env python3

import argparse
import requests
import pickle

REF_URL_ORIGIN = "https://reference.sailplatform.org"
OUR_URL_ORIGIN = "https://k8s-default-allservi-6cf17427aa-1372391052.us-east-1.elb.amazonaws.com"

REF_URL_TEMPLATE = REF_URL_ORIGIN + "/twitter?{}"
OUR_URL_TEMPLATE = OUR_URL_ORIGIN + "/twitter?{}"

def get_url(arg, server_type):
    if server_type == "ref":
        return REF_URL_TEMPLATE.format(arg)
    elif server_type == "our":
        return OUR_URL_TEMPLATE.format(arg)
    else:
        raise ValueError(f"Unknown server type: {server_type}")

def main():
    parser = argparse.ArgumentParser(description="Send requests to a specified server and save results.")
    parser.add_argument("--args", required=True, help="Path to the input file with arguments, one per line.")
    parser.add_argument("--type", required=True, choices=["ref", "our"], help="Server type to send requests to.")

    args = parser.parse_args()

    with open(args.args, "r") as f:
        arg_lines = [line.strip() for line in f if line.strip()]

    results = {}

    for i, arg in enumerate(arg_lines):
        url = get_url(arg, args.type)
        try:
            response = requests.get(url)
            response.raise_for_status()
            results[arg] = response.content
        except Exception as e:
            print(f"Error requesting '{arg}': {e}")
        print("{}/{} requests completed".format(i+1, len(arg_lines)), end="\r")
    print("{}/{} requests completed".format(len(arg_lines), len(arg_lines)))

    output_file = f"results_{args.type}.pkl"
    with open(output_file, "wb") as f:
        pickle.dump(results, f)

    print(f"Saved results to {output_file}")

if __name__ == "__main__":
    main()
