import pprint

from apiclient.discovery import build


def main():
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  service = build("customsearch", "v1",
            developerKey="\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCex7C3zEjpGGm6\nnTagcsodGW/jL2z0qnDUYe2UgBLq46xVu3Ef7LUeM/PQj1F6U7TrmpzRd2ED8jHk\ntTVnJxF8DpEjWUVB3EleybswdIuZkXs/4hWCjILuiMeKSEaMIZEeSzTQs6UoqaKr\n5/XEoL7NfyIDfHjJRWaWCJpHcIgxNnXiYewTR0XxDTGtgaQXm2IW1S1ttQoyfIZX\nnaMNbT5R571bYqSFuPPlmdkFyw6f5L2emQJS/YAJttcpVmCYtINc07D0NPtEaXa5\n+CkWOMjitPR/l9MkMCE70rJkF32PlVvH4ws8xoSbw+6Fp+7/SAwfdXsXkuGZKi8+\n9hMNd4RRAgMBAAECggEAX4qTWJVxDemlvSfadgN8gLQMsmyYKETi7bkbZ28Fcxea\nXGAUuvwJI+po/IcwpOX3iImZcSVfWCuFQDSVtMM6byaoyNdvqCiwcXv7yjVmxvpW\namNVRB/erT/aqefBo5KTKuJgHnDqoaQpgT1rkmyTQz4LroNYfuvmxcLZasFZAhrr\nOsPl9DlVHsrDPXfLDDiucE5fMwIbaHEAjAkj6A9qLKgMZcVVReQ2rWDT0ENgbsTe\nCwQgzCkoVOBZuWb9khtariYs+yETsnI/ItcXeLXr/wSQN9RkFnze9j8J1rAYaPTV\naRMgyj0iqa5j+9YuRrMydDvxljaicmSpsnlvJsLUTQKBgQDTqeEAreFaQPfZWBKe\nkTC8O1ZRQ/l2QKaWfrXu0LU4q7hSvLbqnV/C3Y271hKTYcFk8c1hVSBl2VmmHUkt\n+gB7UFXfDvlgPD8YQYQyAm/EKbJiVz7xgHvj+noDbKZlSrT2st1Wn81bvKE0v81L\naDoQKv8sv6Xl2xJ2g+oSlCJtNwKBgQDACgQHEcOFrTBYA55eYHYe9B0APCJ7R3cI\n7lK++SAOc5FqLfa3zYcudp+i9CUl20SB1u6RgdBtZIvc7DzT1YUFHHzqrcLL2JaW\nmohsyTZrHC/AaIvNhBiktm/nWUWlLxa9rm43WNfqlBkJJt8SdmX4vR4rYM+4lExl\nBp2oj+ketwKBgQClkdBY2KtcD1ARaux9rzNBOuVFgnekQeRN+uZT3lyz7NetmMM4\n+UvMQcS59zXmpeRDE0bF6XIDWabf4y64UUSJMYlKiAsYdWghkDZZbECDYN6SQI8T\nGJ9Q8UD6ZsYum+a8x6OOPEjGhuJPQe3UG763oPqkxXF/QQPLQ1sZl1jqtwKBgBjV\ncr3jSzCPO/A1z5YOzVelY9ay8BaXIEqUXzj5CG81/LkJZp1QQ8n7ZxtwjRk/KLXN\nsJ46dlSfKwMPvbH7K6+Ehpbmj4lC4f5pz3iZ8KKbS4WLP4D9Mx6hxQja34nD9CHl\nW7VmlM1uB2rKjxBZJUisVClx5IrPCq4J0/uHWLMzAoGBAI7pXklkdVy1mNcXUgY+\navM+cAz10IwEQXZSNwk+3rvMmowTt7zimrS1t/WPEylzXx94vo5MgxLRTXgbmDwF\nNsVNbK2mEyfBeMjUlbGdJNkPqk1Pn4ZxV1U4jas2j5eXeoGtG0hpBP5dC5mSEins\nssEV1bdcx5fqjaBg4iqtkRs8\n")

  res = service.cse().list(
      q='lectures',
      cx='017576662512468239146:omuauf_lfve',
    ).execute()
  pprint.pprint(res)

if __name__ == '__main__':
  main()