import test

if __name__ == "__main__":
    response = test.complete_return_request(1254, "Chris", "ER343", "")
    # print(response.text)
    # print(response.status_code)

    if response.status_code in [200, 201, 202]:
        print("Cancel invoice is a success")
    else:
        print("error attempted during the processing")
