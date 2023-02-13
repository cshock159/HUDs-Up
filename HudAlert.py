import threading
import PySimpleGUI as sg
import pyautogui
import pydirectinput
import winsound
import os
import configparser

# Pulling in the config file
configParser = configparser.RawConfigParser(allow_no_value=True)   
configFilePath = (os.getcwd().replace("\\","/") + '/settings.cfg')
configstore = configParser.read(configFilePath)
setting_confidence = configParser.get('settings','user_confidence')
setting_frequency = configParser.get('settings','user_frequency')
setting_chime = configParser.get('settings','chime_option')
setting_auto_close = configParser.get('settings','auto_close')
setting_image_folder = (str(configParser.get('settings','image_folder')))
setting_enable_dev_console = configParser.get('settings','dev_console')
bool()

# Variables used later on
user = os.getlogin()
apexProfile = "C:/Users/" + user + "/Saved Games/Respawn/Apex/profile/profile.cfg"
alertsound = ((os.getcwd()).replace("\\","/") + '/alert.wav')
menuicon = b'iVBORw0KGgoAAAANSUhEUgAABC8AAAQ4CAMAAAAevAYsAAAACXBIWXMAAAsTAAALEwEAmpwYAAABQVBMVEVHcEwWFhYfHx8VFRUZGRkWFhYXFxcXFxcUFBQTExMVFRUUFBQWFhYVFRUeHh4WFhYUFBQZGRkhISEWFhYWFhYVFRUXFxcVFRUXFxcZGRkWFhYTExMUFBQZGRkXFxcfHx8VFRUVFRUWFhYVFRUVFRUWFhYWFhYWFhYTExMXFxcTExMVFRUVFRUVFRUWFhYWFhYdHR0dHR0WFhYVFRUUFBQUFBQUFBQUFBQWFhYUFBQUFBQUFBQWFhYWFhYWFhYWFhYTExMVFRUWFhYWFhYWFhYWFhYWFhYXFxcVFRUUFBQWFhYUFBQXFxcVFRUUFBQUFBQSEhIXFxcXFxcWFhYVFRUaGhoUFBQXFxcVFRUoKCgbGxsVFRUVFRUXFxcWFhYVFRUUFBQXFxcMDAwXFxcVFRUVFRUXFxcUFBQXFxcWFhYVFRX1R1+6AAAAaXRSTlMA9gj4MKhs0FgcvJSA5Ar3Vy4HgX5E0afOMeIdky/PCYBDvOOof+NEHmsbf7v1Q+QKCeD2IFpVVqqSWR+9pfWnGqapukWm5W1CleEe0qqGIxNqvqD3JU7M7gQfzXTCcvtG3Q3Y2YfVsuKWJgwZAAAgAElEQVR42uzdB27cyBaG0VHOUitLgCMs72Y28JZw7/4X8Dwzgq3UmWSzqs5ZQhX9QRYh/n/9Be/l/5wBsJD9/NshAAuJzEunACzgU0TuOAZgvqOMX8HYdxDAXAf/9iIcBDDPbf7Ti4hPjgKY4+K/XEQeOQtgput4lgcOA5gpfvcib50GMMNT/AnGheMApnvMeOHagQBTPbzqhXeqwFSH+boXT44EmGIrXstHZwJ86DTe9uLBoQAf+ZrvepGHjgX4wPG7XkRsORbgvd0PchFx6mCAd84+7EV+dTLAG5P4UB47GuCNmCJ3nQ3wysnUXpw5HOClq4ypJo4HeOFuRi/8GQnwwmXO6sWJAwJ+25mVi8grJwQ825+Zi8g7RwQ8yzm9MHcGPNuLOcydAf85ypgbDHNnwD8OFuhFOibgz6DZbHsOCvg9aDbnJwxzZ8C3WIi5M+A8F+yFuTNo3v2CvTB3Bs17XDQXv3xzXNC0hyV6kefOCxp2mMv04t6BQcO2YhnmzqBhP2O5Xpg7g2Zt55K9MHcGzTpeshfmzqBZu0vnIuKnY4Mm/VihF7nt3KBB+yvkwtwZtClW6YW5M2jRSawkfzg6aM1VxorB8Gk+aM3dyr0wdwaNucxVe2HuDFqzs3ouzJ1BW65jDebOoCmxVi/MnUFD9mK9YJg7g2YcZazp2iFCIw7W7oV3qtCI77l+L8ydQRu21s+FuTNow2l0wNwZtOA8O+lFfneUUL37TnoR6dN8UL3HbnLxy6nDhMo9dNYLc2dQucPsrhfmzqBu0SFzZ1C1m057Ye4MKradnfbC3BlU7LjTXvgzEqjY565zETcOFSq103kvzJ1BpfY7z4W5M6hVdN+LyM/OFSp0Ej3waT6o0VVGL8Ewdwb1OeipF96pQnVus59emDuD+lz0lQtzZ1Cb6+iNT/NBZaLHXuSt84WK7EWfwbhwwFCPo4xemTuDenzpuRfeqUI1DrPvXpg7g1psRd/MnUElTqP/XnxxzFCD8xygFz7NB1W4H6AXEebOoAK7g+TC3BnU4GygXuRXZw2Fm8RAfJoPiheDyV2nDUW7GbAXZ44bSradMaCJA4eC3Q3aC39GAgW7zGF7Ye4MyrUzbC7MnUG59gfOReSdQ4dCxeC9yEunDkX6FIMzdwZlOsrYQDDMnUGJDjbSC+9UoUC3uYleRHxy9FCci83kwqf5oDzXsSHmzqA4sbFemDuDwjzF5oJh7gyK8pixQebOoCQPG+2Fd6pQkMPcbC+eXAEUYys2Kx/dARTiZ2y6Fw8uAcqwnRvvhbkzKMTxxnth7gwKsTuCXET8dBFQgLNR9MKn+aAAkxgFc2dQgBgJc2cweiej6YW5Mxi5q4zRmLgOGLW7EfXCn5HAqF3mmHpx4kJgxHbGlIvIKzcCo7U/qlyYO4Mxy5H1wtwZjNZejIy5Mxiro4zRBcPcGYzTwQh7ka4Fxug2x9eLiD0XAyN0McZcmDuDMfoWo2TuDMbnPEfaC3NnMDr3I+2FuTMYncex5uKXb64HRuVhxL3Ic/cDI3KYY+7FvQuCEYlRM3cGI3Iz8l6YO4PR2M6R98LcGYzG8ch74dN8MBq7489F3LgmGIUfBfTC3BmMwn4BuTB3BuMQJfTC3BmMwUkUIX+4Kti0q4xCguHTfLBpd8X0wjtV2LDLLKUX5s5g03bKyYW5M9is6yiIuTPYqCiqF+bOYIP2oqxgmDuDjTnKKMy1S4MNOSiuF96pwoZ8z/J6Ye4MNmOrvFyYO4PNOI0CmTuDTTjPInuR310dDO6+yF5Ebrk6GNpumbn45dTlwcDOiu2FuTMY2CSKZe4MBhYF82k+GNRN0b04c4EwnO2Mok1cIQzmuPBe+DMSGMzn0nNh7gwGs1N8L8ydwUD2i8+FuTMYSpTfi8jP7hEGcBIV8Gk+GMJVRhXBMHcG/TuopBfeqULvbrOOXpg7g/5d1JILc2fQt+uohk/zQc+iol7krfuEHu1FTcG4cKHQn6OMqpg7g/58qawX3qlCbw6ztl48uVToyVbUJh/dKvTiNOrrxYNrhT58zQp7kYcuFnpwXGEvIsydQQ92q8yFuTPow1mlvciv7hY6NolK+TQfdC6qZe4MOnZTcS/MnUGntjMqNnHB0KG7qnvhz0igQ5dZdy/MnUF3durOhbkz6M5+5bmIvHPJ0JGovhd56ZahE5+ieubOoBtHGQ0Ew9wZdOGgiV54pwoduM0WehHxyVXD2i7ayEXkkbuGNV1HI8ydwdqimV6YO4M1PUU7wTB3Bmt5zGjINxcOa3hoqhd57sZhZYfZVi/uXTmsbCvaYu4MVvYzWuuFuTNY0XY21wtzZ7Ci4+Z6Ye4MVrTbYC4ifrp4WMFZk73waT5YwSSaZO4MVhCNMncGSztpthfmzmBJVxnNmrh+WMpdw73waT5YymW23IsTDwAsYaflXEReeQJgYftN58LcGSwjG++FuTNY2F40ztwZLOooo/lgmDuDxRzoRabHABbxPfUiYs+DAAvYkoswdwYLOdWKf3th7gzmOvfTxfNvML57GGCOe714DoZP88Ecj3Lx26nHAWZ60Is/P2GYO4NZDr1LfdELc2cwi0i8Coa5M5juRiNe9cLcGUy17T8jb96pmjuDaY714i0PBXxsVy7eufFYwId+6MX7/5KYO4OP7MvFB70wdwYfCb34KBjmzuC9E234sBc/PBrw1pWfLqYEw6f54K07vZjSC+9U4Y1LfzgylbkzeG1HLqb/hGHuDF66VoUZvTB3Bi+Jwsw/IzF3Bn/sicLMYJg7g98Mms1z7SGBZ1/0wt+pwmJ8hG8+c2fwny05mP8rDHNn8A+DZov04osHBQyaLfpO1af5wKDZosydgY/wLczcGZzpxaL/JTF3RusmOrBwL8yd0ToZWCIYPs1H2wyaLdOLMw8MLTNotpyJR4aGGTTzZySwoM9ysSRzZ7TLR/iW/hWGuTNaZdBs+V6YO6NVBs1WCMZnzw1NMmi2Si98mo8mGTRbLRjmzmjRgV6s1AvvVGnQrY/wreiTh4fmXMjFqj9h+DQfrTFotnovDjw+NMY/+9V7kbeeH5ry5J/9GsG48ADRkke/vFiLuTNa8qAX6/EI0Q6DZut68hDRDINma/8K49FTRCMMmq3fiwePEW346j8jHbxTNXf2f/buBDmO2wzDsKjVskhx36q4FslLJbmA5v4HSDl2HDuy6Fm60cD/Pc8N2AOAM90NvGRwCN8U5M6IIGg2DbkzEgiaTfST5N5YojxBs6nWC0fzUZ+JPtmCIXdGdYJm060XcmcUJ2g2pSMDitIurBe2kcB6jm0cmZTcGZUJmk18C0PujLoEzaZeLy4MKsoSNJt8G8mxUUVRNyb45AuG3BlFffbtYoYFQ+6MmgTNZvlFYmBRkaDZPD4YWhQkaDbTNwy5M+p5MLNnWi/kzijnq28Xs93BkDujmkvrxWwLhtwZxQiazenBAKMUQbNZv2F8NcIoRNBs3vXi0hCjEEGzmRcMuTPqeDGjZ14v5M4owyF88z9TlTujCkGz+cmdUYSgWQsvBholCJo1+UniaD4qEDRrs17InVGBqdxowZA7Y3xfzORG64XcGcM7cfOimSPDjcEJmjVkuDE2QbOWvhhwDE3QrOktjBMjjoGdmsNN1wu5M0ZmCrddL+TOGNgHU7jxgiF3xrAEzdo7NewYlKCZZ6qwpkfPUhcgd8aY9iwXS9zCkDtjRPvm7iLrhdwZAxI0W+qZ6qPBx3AEzZZaMBzNx3AEzZazb/gxGEGzBb9hyJ0xFkGzJdcLuTPGYtIuumDInTGSM3N20fVC7oyBCJot/UxV7oxxCJotziBkFIJmyzszDBnEk/Vi+Z8kcmeM4aPlooP1Qu6MMXyzXvSwYMidMQJBsz7WiydDkf4JmvWyYHw0GOmeQ/h6WS88U6V75zaOdEPujN4dWi76+YYhd0bfBM16Wi8czUffTNKe1ovVuRFJxwTN+lowDg1J+iVo1hu5M/p1Z73ojUFJrxzC1x+5M3q1Z3r2dwtD7ow+CZr1uF7cGZj0SNCsz2eqjuajR4JmfZI7o0MO4euV3Bn9ObBe9PqTRO6M3hyZl92uF3Jn9Ma07HjBcDQffRE063m9ODBA6YmgWd+ODFE6ImjWOUOUftxaLjond0Y/3lkver+FIXdGLwTN+l8vLgxTOiFo1v96sTo2TunCjek4wILxzkClBw7hG2PBkDujB4JmY6wXnqnSAUGzUdwYrCxO0GyYbxiO5mNpgmbjrBdyZyzNNBzomarcGct6Ng0HWjDkzljUtZsXQ5E7Y0lX1ouxGLIsR9BsNM8GLYsRNBvuFsa1UctCBM3GWy+uDFuWce/HyIDPVOXOWIZD+EYkd8YiBM3GJHfGEgTNBv1Jcm/s0pyg2ajrxc8GL82ZeMMuGHJntCZoNu56IXdGY4JmIzsygGnqwnoxMgOYlo5tHBnaF0OYhgTNBr+FcWIM04yg2ejrhdwZ7fg1Mvp6IXdGMx9MuOEXDLkzGhE0q7BgyJ3RhqBZiV8kBjItCJrV8MFQpgFBsyLfMOTOmN+DmVZkvZA7Y3ZffbsocwdD7oy5XVovyiwYcmfMTNCskgcDmlkJmpX6hvHViGZGgma11otLQ5oZCZoVWzDkzpjPixlWbL2QO2M2DuGr90xV7oy5CJrVI3fGTATNKnoxsJnFk/Wi4k+St0Y2M3AIX831Qu6MOXyzXtRcMOTOmN4XM6voevFkcDO1E98uyi4YjuZjaoJmddcLuTMmJmhWmdwZ0xI0K/0NQ+6MKZ2aU6XXC7kzppQ2f/6Z9XVK7owppQXN/vWPsJ9fcmdMJy5oFri17tQwZyJpQbOjN2/u4+7vGuZM4zHrWerq4Jc/ej9tvZA7Yxp7YTf/ft1PkXb0oNwZkwj7T/vf/ZppRxvLnTGFtKDZ6v63P/wu7Znqo8HOztKCZvupT4VWjuZjZ2lBsz9MmrS3Tv63VMKWsoJmfz4vO229kDtjR2F3/VZ3f/zj03bNyJ2xo+yHiodptzDkztjFWfZLS+dpz1TlztjB27yNI3/2Ke2ZqtwZ20vbdfXdpqsT20hgTbdh/10Pv78Ecaeinxn2bOld2LPU87+64Zt2y1PujO18tIEir+omd8a2z1LD1osTX7J+uQy3Rj5bSPvp/sVNnP+sF47mYwthjwZ+HO1Je0gkd8YW0l49+OEsSXsJRe6MzYW92vjat/C0l1zlzthY2NaJV+/ypa0XcmdsKGxr5utPEY/S1gtH87Hhs1RvKf3BQdo2knMzgA2kHS31N29Bv0+75XloCrC+z+n7Uv/fpdwZ/MhdXtDsdV/tU4Uf+CkxaPY6uTP4gbC0129BM9fkTxdF7oz1pAXN1jrlNi53dmcisI64oNl6p+jfOZoPPAtYs9IT98xI7ow1hL1rsH4FUO4MvnMQdgjf+pXhtPVC7oy/FbZXYpOtEnJnkP1PdKPHhnFH8703H3hVeNDsdcdpz1QPTAhe89bGkddcpF2eI1MCE+J3G26rkjuD2C/cmx+FLXcGoTf0VqvjzW8Hy53Br9KCZhcu0RzXiJRnqYJmf+spbRvJsXnBX7oJ+22+1bH57+XO4E3chqptszxyZ/BG0GxNcmeQFzR72vZCxeXObkwOvpMWNNt+b0TaeuFoPr4jaLa2uKP55M4I/6e503tIV3JnZHsOWy92es/5Wu6MaNf2pW5C7oxoV2EbR3Y8+1rujGRpQbOrXS9YXO7s2SThd2lBs+vdr9jKJSOUoNnGHtOeqV6ZJvzqXtBsc5/kzsiUtoPqYYqLJndGprSg2UQvE8Tlzl5MFd7kBc2mellx5Wg+8giabSnuaL6fTRYEzbYmd0actBPyP0x36eTOSHOS9lhwyosnd0aYC4fwWWzXZ8JkEzTzY24TX0yZaIJmbhZvdAVPzJlggmY7OkpbL+TOkq0EzXZ0IHdGirRXmmf49S13RorPDuHbndwZIcK2ZM/z9kBc7mxl4mRKC5rN9HbiS9ozkg+mTiRBs2mEHWYod5bpIWyUz7a7Uu6M+tKOxF/dz3Yp5c4oLy25sz/fpZQ7o7q0Mb5n7Z3QgwkURtDMb7sdrudXMyiKoJl7x7tcz0tTKEra+J67znUod0ZdZ2Hrxez1z3O5M8p6a+PI1OTOKCttj9Tp/Jf0s6P5KErQbAY3aevFmYkU4knQbI5byHJnVPTRdgeXdYLrKncW8iw1bL1otZ1S7oyC0s7Av2l1YeNyZ08mU31pQbOG9/EvHM1HNYJms4k7ms8z1fIEzWaU9tqs3Fl5gmaz3koOI3dW3GnYeG6c45I7o9azVO8UzUrujELSgmbN31mWO6MOQbPZpW3la7GXj4UIms3u3j5VingUNJvfftp6IXdW1Z6gWYurnHZPWe6sprD/fEudSSt3RgVxQbOlzryPy509mlwFCZo1Epc72zO56nkvaNbKc9otz33Tq5wDQbNm0tYLubNywnY2rO6WvNinaeuF3Fk1HvK1dOhoPkaWdjLDwi8RxeXODkyxSgTNGkt7836JV++ZjaBZY3JnjOtW0Kw1uTOG9U7QrP0NZrkzxiRo5qLPf9Xlzso8Sw1bL/o4hDYud3ZrppWQFjTr5JD7W0fzMSBBMw+l2lx5ubMKPgmaLUPujPGcC5otRe6M4YRtZejqrlvaeiF3Nry0oFlXT/XicmeO5hv+Waq3hhYUlzs7N+OGJmi2qLjc2aEpNzJBs4Vdyp0xjjuH8C3rq32qDCMshbG66u8jkDtjGGGprdW1z2D5D0HubFSCZr7jtf8U7ky8Md0LmrmH5CYSa/pZ0MwzqgXInQ0p7Nl/v1W+tHdg5M6GlBY067f6m7ZerO7NvuGkBc063roQlztzNN94PMbrh9wZnRM064jcGX0TNOuK3BlduxA068mJbSR07NghfH1JO6Nd7mwoaUGz4/5vP8ud0au0oNmFj8Rngn9ma47NEY6ZfUrbRnJsHg4irQ0+xDH27+XO6NJnQbMeyZ3RJUGzLsmd0aO0oNnTKB9MXO7sxmQcQFrQbJy9CmnrhaP5BiBo1q24o/nkzvwT817Q9q7kzujLc9h68TLSh3Mtd4YRuaDBzoqMy509mJK+8Xb0hXews6jjcmedntlO5B21HoNmr0vLnfXZhOE3gmbdf0IrHxGdePHPq3ePac9Ur0zLXr0VNOvfJ7kz+pC2o2nIm+9yZ/QhLWg26MP9uNzZi6nZpbSg2agvD6atF47m65Kg2SDkzvBvq/koHHfz4zu5M5aWdmL9h3E/qmO5MxZ2kvaYbuQP60LuDEOw5Xrx0eI+EhPUV9wll4vBD5+Oy519MUXdQlvw18jocYu4Z6on5mhHBM0Gc5S2Xsid9STthvv4bwAdyJ2xlLRXjAvEv+XOWErcFqYKH5rcGQsJ2yJd42l+3OEDKxO1D2FHsFR5WzDscKOh38gtZU/QbMzPLe0ZidxZD8KOkK2z21HujPbSjqhf3Zf56OJyZ4+m6+LSEjj7dT66uNyZo/mMucb2rPUWe3ynXfMrbanTpuXOcM9szvFWrGbxkLZeyJ0tK228VatlHcqd0c5Z2HrxXO0DPJc7o5m3No6MTu6MZtL2LJ3W+wg/O5qPRgTNCojLnZ2ZuAt5EjQrYJV2y1PubBkfbT/wMQ74OcqdLfQsNWy9qLq9Ue6MBtLOpL+p+kHG5c6eTN720oJmhe+rXziaD4PMGLP0x639vsT2McRKHy8td4abZJOuF7e1b12HkTtr7NQzuErkzvAPyTs+a5M7Y0aCZsXInTEfQbNy0rYOVtw72K07QbNq7u1TZSY/CZrVs5+2XsidtRIWxgrZbyB3hv9EE4yrkDNi43Jnd6ZyC3FBs5Qz6K8czcf0BM2KSktPfZM7a+C9oFlVz2m3POXO5ncgaFZW2nohd/Zv9s6tuY3jCKMLUCQIkiAAUQBBBVeTtC1fEvtRlbwnD6lKVSqVPOUeO+H+/x+QlEwpFAQCe5nd6Z7vnJ+w3dO72zPTp3HEbhpoNcWu1OoFujNeQWy6VWfIaD4IiZrQTOxQj5zubMCSbhKEZonTUwvwiEXdIAjNEgfdGYRjgdAsdeZq9QLdWXMcITRLv6GN7gzCgNCMIKcXZXRnvHrCZJLmUFg53dmCld0IalPnRYfOy+nOGM3XCAjNREB3BgHoITTToIvuDGojdvRPWcqrdogX3VkDiF0tkL5ZoFYv0J0FB6GZEHK6sx4LnFcOp3gqI6c7m7DCg6I2ekn8lLCc7mzIEg/JDfdStbhGdwbVmTGET4tL7qlCZdSEZjNCLqc7uyPmwVATmt0Qcj3dGUHnXVMtc5gCmwnqzvioDMQKoZkiS3RnUIUzhGaK9NGdQQXE9uJz0uaRY7WWJy+KEKgJzTaE/BG1epGviHlt1IRmXCX4gJzujNF8vGTK5kyfkH8A3RmUBKGZMOjOoBwIzaRBdwalmCI0U+Yl10igBGKzohkVvY3aTHh0Z7VQE5qNCfl2uxvdGRRFTWg2JeTiKUAO8HIpniuMfVX/xOQbswZqrm7Gyu9gofaBQQ+rIn32UkHvuiG6s4qobb6PCPku5HRnOTGvgprQjLN9zyCnO+OMbxUQmsFj21sM7hBVYC2WI9xNfBa50XzcUS7NJed04D0zdGewHzVhzT0hf54bdGdAhjyBIXy8PZ6yJuZ8ge75AGU2NH+nH2UEM+LpcD2fHbgnDqCmO8NBUwqEZrCVETkpAc9wz8sEPmaD7gyeoYvQDLbpoTuD3ajdMKIZXgB0Z7AbNaEZm+2FkNOdcSSnGGpCMw7zFUOtXnDktxAIzWAn6M6A1wiXEQtzhO4MtlGbID8n5EUZozuDLcQMNTlD+EowRXcG0inBsEZeJvsg5nxyPi0XDIPmZ3UfjIynpfV0LxXZRMlmuFrLEyXNPhCaAQlChhRFrQHOiZyy3KI7g/eoHflFxl2aF+jO4BGEZnAQtcuID1fE/BkQmsFBuuypwjs2CM3gMOjO4B0dhGZQALV6wQ2jnYiNdOX2YVXQnYGg0GxFzCsipzvbEPNPUFPSXBDyqsjpzhjNJ58DpADvFl4ufGMW/cRk+jP/riXyhQny0j0s7BL1WKvVCww10ntk2KtqMkR3pozaGZw7Ql6PCbozYbpcHIFyoDsTRu0OEVeIatPnGoksCM2gNHK6M4YfvOcWoRmUJldreTJc6SdOuA4ApM3BvOHC0eNeqli9YIRrGNCdSaI2I54R8YGQ053dEnOEZlAZNd0ZcqtMbyOdmPOq4V1TmQlCM+BXln/ZgohdBMgXrPKQrXIx5HvlV+yJQXVGavWixwuCMzdQmYHaNRLts34IzaAWcroz6bsECM2gJujOhFgiNIN6oDvT4RShGdTlXq1e6OrOOmL/npz/J4sCpJGq7kxNaMbMVr5SQ+TRUjPOckIzZsI3w4zRfAogNIMgqKmuNF1XLxCaQRju1Fqeiq+eAUIzCIRavRD8tRU7+a/apGqHK7V6cc0rgU0wqMyQ0XxpoyY0O2ZNN4mc7kzs6B9CMwhKTy2hRlLhRWgGQUF3ljILsa9HhvA1zlytXiiNRjgS20sds56bb6CjO0sVNaHZlNVMUgXPqjNeBYlGFqEZH60NpJXK6Gi1X02GwLeCnO5MpCvWR2gGTYDuLEkQmkEjdNGdJYia0AxJbmuoHRp+mAsEVU1oxhC+FhvpYgjcSkJoBo2B7oxXAKdqoDDozhJDbRQSQrNWQXeWFjfcS4UmQXeWFDOG8EGTrLinmhBqQrMZC7htLtTqxV3CwVQTmt2wfskxkozaXyySCM34huUjln/LopFEaBaDJbozetceQWgWhT66syQQ2xvPEZpF4lit5Znmi0lNaLZh5UZCrV7kqwSDqCY067FuYyGnOzuj6LuPIUKzeKA7cw9CM2gNdGfe6aptcrFoY4LuzDlThvBBe7zkGolrxGY3IzSLzblavUhrCD1CM2i5va7W8kxJcoPQDEg5cq4oOUIz4JOWb9piqB3QRWhmgIXaB0YyPbM+Q/igfc7QnflEbTN8xFq1gJzuLJEzP2pCswFL1QZyurM0zhQjNIM4qNWLJO4srcVihtDMDOjO/HGp9heJ0MwO6M7ccS1WL+5ZpXZAd+YNNaEZQ/h4W8Vk7TxgCM2Av+EWM9D3THqEZhAVNd2Zc+cNQjMgA0nBgtyLBeuO9ckXLp+4VelycQRig+7MDWo3fq5YnfZAd+YFNaHZkMVpETndmdcjQGpCswlr0yRq9cLpEWOEZmACdGeUdYNRQmhmlSN0Z/ZRm+g+Z11aZay2p3rrL0ZixpicvVTDTBnNR4iIEPDySuTthdAM+DmOh7cR9QjNwFTzHd0ZW1h2ooPQzDjozthL5YQMFOYW3Zld1I7gvmI9WucFujOzIDQDc6hdfnR0+xGhGZhDbriCm7fYBqEZ2APdmVE6CM2AJnz8xPRxo0lsxCpCMy/IjeZzcWNaTmi2YiU6Yaa2p7pxEBQ1RcwF69ALavKsvENMrIHQzBFyujP7LzOEZsC/spn8tK47UxOaLVmEnkB3xp4VW1ZQmI5aC8O27kztTMwxK9AXG3RnhkBoBsbpoTuzA0IzME6fayRmWCA0A+vI6c7sDls4QmgG5snVWp5WhzmdcDwf7CM3ms/qBSexmarORqqC5mfw/xJ1YTIMajPbz1l5PpHTnZkczYfQDJyA7swAPYRm4AN0Z/GZIDQDL6A7i85Q7PNiwapzjFq9MNebVxOaMYTPNSO1etGjYHMGBiozULtGYutsIUIzcIWc7szU3QWEZuAMdGcRWSI0A1+gO4vHKUIz8Ma9Wr2wM9upI/YviNAsBcSy1s7sSDWh2TVrLQXkdGdGZlPLCc0uWWtJMGM0XwwQmoFL1NRaNtxaYjvZOUKzZEB3FoGB2BC+DessFdCdtY/YSXyG8KXEWq1exG/VsykFfhmq9epjHwVAaAaOmajtqUY+aojQDFzTU0vgUdTHPUVoBp5Bd9YmY4bwgW/mavUi5igGNU8M84MAAA2wSURBVKHZmPWVHA/oztpCTWg2ZXWlh5zubEppbulJIzRLkSO1aySxvpLVfv0QmiUJujNay008ZvZSEwXdWSsgNIMk6KI7awE1odktCytV1A4pP8wjPGQ1oRlD+NJFrV5EuAWF0AySAd0ZJTmZUy7QPOjOGuZOrF4gNEsadGfNcsO9VEgJdGeNMhO7OHLKikqbFfdUG0RNaDZjQaXOhVq9uGvx4aoJzW5YT8kjpzu7oRY39GQRmgkgpztr7aN5hdAM0gPdGb3kIKxZSwqgO2sGNaHZkKWkgdqZoof7Vh6rmtBswkoSQa1etHJoGaEZJMqVWr04owgHf6YIzXRAdxacc7F6gdBMCHRnoXmptunEIlIC3Vlgpgzhg3RBdxYWhGaQNHK6s2aH3iM0g7SR0501KdVBaAaJg+4sIDlCM0gcdGfBOObfDlJnofaB0ViPrs8QPkifM3RnYVDbnB6xdhSR0501dMZITWg2YOloIqc7a+YMM0Iz0ECtXjRyR2ot9gwRmsmC7qw+l2p/dSvWjSzozmpzLVYvLlg1uqA7q4vacMMOi0YZtbdj8Bm1asOT/8aakeavai2MsDPw5eQMv/9Tzyu//fu//hF9vf37Pz/2/DL78x/U6kVYx46c/Mkz/7Twgv4h943cnmpI3dn9A7gJ/BsjPcMOsfCUNgF1Z92c5+mF13bmE88fyBtHX9ThdGdnxN0Lc1Pbkt8SEEewGy3XdPnC2DbDr0gdP7wKFPRbgu6jXBhUK/2cuPhJoDC6sxPKhY9wv8ks8k1O/jhJoDBXpuhaueC1VRHbr3MqhpOCEeJK9jnP0QPzzCzf9ygYPurFbf1gvyTUDjoX5hqd/NK6TKT6o/mmhNp+uTDvkP/yF4TJQybV3lMd8ylpP8pvMvtcECcP1B2Jf0S5sI7ZRufH9F8TKgfvnnrKnSueoPUvSD+SlHN22uznUz3dGQ/QenwXjoZKcAXNQS+sju7smAdoO7jfOBtD85agWc+pGrqzPt+PtmN7knnjC6JmnavKwe1RLyzz+ZeZQz4jqYxTNbIb9lINf1u4tUH/hvPhtqmqO+sQVsP1YpF55TvOh9tOrWob9JywsRtRd43O7fPhVAzD2VXpuPAlEbUb0ZPMN98vyS7Db6NNhZBeE1Eanc2xJox2C0YFWxdD+Gh0Nns+/HNiaZbyNtAB9YJGZ7N8TRPDbJKV1Z2NeGY0OjkfLptnZXVnPDIanS2AosRqopUbzfeKJ0ajs5VPDBQlNuvFoEwUEZrR6GwLFCU2GZWIIUIzGp2tgaLEJsUjuKBc0Ohs8woa8TVIcd0ZQ/hodLbKKefDDaZcUd0Z099pdLbMJVfQ7NWLoroz9rhodEa4gkagfTbMEJrR6IwAihJzeVdoNB9CM2N8lonAAAWPTTOG8Nn6FznNZEBRYi35DsdsQuPJEoNVpgSKElscbpwNCZid+p5/nYnBFTRbGXhId4bQzBDfvsj0eEvcDdWLQ6P5eEQ0OiODosTSF+5kb6wQmtHoNHA+nH9iM2k43NugJlA0Oi1cQeN8uBn26c6Y2kyj0wacDzfD3ms/PB4anUbOh5OMNnhed8ZeFo1OM6AosfKx2+c8Lo1OB6AosZGQy93hWVHPaXTaOh+OosREM233C4whfDQ6uYIGn7JTd4bQjEanPb4akhTx2aU7Q2hGo9MiKEoMfPZ++o+M0IxGp9EraChKoqfmGRdHaHS6AUVJ9IKx/Z+M0IxGp+Hz4SRI5PTc0p0hNKPRafsKGikSl9FH4ZhSL2h0mgZFSWSeBmNMLGL+iuQ0Og+DoiQuT3VnCM1i1ovlJdWg2BU0kiVimnYJhAnWVIKCoCiJWS+m/99LpV5Eo/MVdYDz4S5+m8cfTtBBLI6pAeWuoKEoiVYwHnVnDOGL1+jcUAHKgqIkWr7+pDtDaBat0fkdy7/C+XDGOkXK13d7qgjNaHQ64y25E4d5htCMRqc/UJRE4pfZX3gINDodng/nLReD33EvlUanzytonA9vn59l2R95CjQ6XcL58AjlIstOeQ40Op2eD6ditF4uKBg0Ov/b3rkuRXVEUbiT4sBMOcT8Pkdiwo8BBDMGuYmlogiJWkmZSqUqr8C8/wMkRVJGuc2te/e+fN8TUIvudc6s072XVagoqWAXKe2jBUGnTagokbeLlE5Qg6DT6PlwKkrE7SKlDj0IOo3CFTSJ59yVTkQMg6DTKlSUlPeLa9MiMQyCTrNQUVKY4+ua7+0iC0GnUagoKcrN4yKZLEDQaRYqSqTtAsMoaRcrBJ2Fz4ezyoTtIqUh5+UK+cUWG7o4VJQI2wWjcwrR9tnNAlBRImwXKb1GoPw8YCvLQEWJsF2k1CBR7qBzg40sBs0YsnaBYWQPOtnEklBRImsXKR0hE0GnYTgfLmoXKR0gFEGnYagoEbULBmIQdBqHipIcHEz/YQqxCDotQ0XJ4hzNoPcx36UIOk3zjCW4GLPddlrCLwg6TUNFiaBdpNRHMoJO21BRImcXDMQg6DQPFSVydoFhEHTah/PhYnbBBB2CTvtQUSJmF4mBGASd5qGiRM4uMAyCTvtQUSJmF0zQIei0DxUlYnbBBB2CTgdwBU3KLpigQ9DpACpKpuRsca0ZiEHQaR8qSqbhPIfUGMZUQWfHptTM0lPW6MQ1nEdqJuhMfLe4uMeO1A7PPRm7YILOZL9YYzvqhytoMnbBQIwJQecOe9EGVJSI2AWGcadfLLMRrUBFiYhdYBi3M9xkG9qBihIRu0jpLZoSdHpgGcMQsAsm6BB0OuHrVdZtebtgIAZBpxc4Hy5gFxgGQacXqCgRsIuUnr9EXIJOF1BRUt4uEgMxCDq9QEXJf7wsKjOGQdDpBK6gXfI8YRgEnTCZNfzi4qL4NclzNCbodAIVJQK3qs8IOtlpToheUSIyhCH0xWCCTl+EPh8uNLMlsmEQdDojcEWJ2IinX4NKTNDpkJ+ivmIIToT7PahfEHR6ZGuMXRTm24gKjwg6fdINsYvChBuIMR5vs7HcMsAuMIysPF5iVzkmWEVJhWn2sSborLOlnBPpfHiVlt9+oEMXPfaTe+JUlLytFBNF0Xf1IbspAkEOFlV7+IUwDILOOGxgF0WJMEGHoDMS69hFUdzfbyfojIX3ipLaSZxrwyDojIfvipL669mzYRB0RsRxRYmGx9+IoBNc4baiRMfb8guCTvDFALsoiMvv1gSdkfFYUaIni3NnGASd4XFXUaJpRb8h6ARnOKsoOeQHH0EnlMTTFbSBMm0PCTrBG34qSt6o09bNQAyCTviEk4qSRqG0LgyDoBO+wEVFSaNS2n2CTvCH/fPhjVJlHxF0gj+sV5Q0apU1PhDjKUEn3IDtipJGsbIdPgwOMVxRontVfzD7U2T8A9sCbn0QDrGLMry36RffPWFTwB0MsIsymLyp8z0bAiak+fexCwzjkq8esR1gIubOhxtJ5Ea4MHjEWEXJCyu6GpqgQ9AJM2BpcsMIWQk6oS52KkpafJigE6qzjl0UwMYEHYJOmBkTFSWtNVUtfK8m6IQ5MFBR0tpTVfkEHYJOmBvtFSWtRVF1D8Qg6IT50V1R0toUVbVhEHSC09/brVVN9U7QIeiEBVFbUdLa1VTrBB2CTlgcnRUlrWVJFQ7EIOiETGisKGltS6rPMAg6IRvqrqC9t67oprZPTwSdkA9tFSX2Ff1mV5Oe9wk6ISuqKko+eFBUUZD8jPUNmVFUUdL5UFSHYfzzb91gdUN+tJwP77wIOlJhFyusbCiCjoqSzo+gpwr8Yot1DYXQUFHSeRL0VfXv0n1WNZSjekVJ50vPyhN0HrCioSiVK0o6b3o2FZMLgk4ozwC7yMk7gk5wTb0raJ1HOStN0CHoBCkqXUHrfKpZZSAGQSfIUaWipPOqZgXDIOgE5zndiV8x94WTC4JOkEa6omTfs5gnBJ3gHdEraD3fWgoOxCDohDr8Inc+vOddSzHDIOiEWjyROh/e86+l0AQdgk6oiExFSS+ClOUn6BB0Qm0kKkp6QbRsCTrBPQPswoZhEHSCBvpD7CITI4JO8M92wRSjF0rJU4JO8E+5ipJeMCVLTdAh6ARNFKoo6YUTsikRdO6wQEEXRSpKDgMKmd8wxsssT1BH/vPh70LqeJRZxeEmaxMU8mPmhR61L/wg57vFxT0WJihlJ+eHkiasjBkHYozXWJWglp/zXUFrAsvYI+iEEGSrKGlCy3icRUWCTlBPnoqSJriKS2OCTghBjoqSJryKfYJOCMIAu8hguwSdEOXh2GIXNQ2DoBNssUhFCXbxL3u7BJ0QhPkrSrCLT7QEnRCFOS9CvEK5hQyDoBNsMldFySm6fc5w5oMYBJ1gldmvoI0Q7UtWxgSdEIVZK0paJLvKa4JOCMNsFSXYxQ00BJ0QhxkqSrCLRQyDoBM8MHVFCXZxC0cEnRCIAXaxGNNM0FlHJnDCNBUl2MUd9Cb+FukhEvhhYkUJdrGIYaw+RCLwxISKEuxiAndM0BmPt9EHvHFXRQl2Mdlwb1Xv8RLqgD9uryjBLqagT9AJsbjlfPguykxDR9AJsbi5omQPYeY1DIJOcM0NFSUdqkzJlQk6BJ3gnmsVJdjFDLQEnRCLKxUl2MW8hkHQCSH4vKIEu5jPMAg6IQz/V5RgFzNzTtAJ0RhgF3NzNibohGBcVpRgF3Pxx19/IgIE47eLjzr/sL8BjZNyYJpcHQkAAAAASUVORK5CYII='
image_file = ""
default_font = ("Helvetica","10")
header_font = ("Helvetica","16","bold")
options_font = ("Helvetica","8")
subheader_font = ("Helvetica","10","bold")
statusbar_font = ("Helvetica","7")
default_padding = (2)
if setting_enable_dev_console is not '':
    default_window_size = (500,360)
else:
    default_window_size = (500,260)

sg.theme('DarkBlue14')

#### Add support for 2560x1440

# Layout building
start_stop = [
    [sg.Text("Start/Stop",font=header_font,p=default_padding)],
    [sg.Button(button_text="Start", size=(10,2),button_color="Green",bind_return_key=True,tooltip="Start HUDs-Up with the options chosen below.",font=("Comic Sans MS","10","bold"),p=default_padding),
    sg.Button(button_text="Stop", size=(10,2),button_color="red",tooltip="Stops HUDs-Up.",font=("Comic Sans MS","10","bold"),p=default_padding),
    sg.Text("Start will run the program with the last \nknown settings, or defaults if first run.\nSettings are auto-saved on exit.",font=subheader_font,p=((25,0),(0,0)),justification="center")], 
]
 
audio_autoclose = [
    [sg.Text("Options:",font=header_font,p=default_padding),
    sg.Text("You must click 'Update Options' after changes are made.",font=subheader_font,p=default_padding)],    
    [sg.Text("Detection Sensitivity",font=default_font,p=((53,40),(0,0))),
    sg.Text(("Time Between Checks (sec)"),font=default_font,p=((80,40),(0,0)))],
    [sg.Slider(range=(0,1),orientation='h',tick_interval=.5,resolution=.05,default_value=setting_confidence,key="confidence",tooltip="Determines how sensitive image recognition is. Higher = Less Sensitive.",font=options_font,p=((40,50),(0,0))),
    sg.Slider(range=(0,10),orientation='h',tick_interval=2,resolution=1,default_value=setting_frequency,key="frequency",tooltip="Determines the frequency in which HUDs-Up checks for the HUD.",font=options_font,p=((50,40),(0,0)))],
    [sg.Text("Browse for a custom images folder for detecting the HUD. JPG only.",font=default_font,p=default_padding)],
    [sg.FolderBrowse(button_text="Choose Folder",size=(12,1),tooltip="Choose the image folder",font=options_font,key="folder_selection",p=default_padding),
    sg.Checkbox(text="Audio Chime",default=setting_chime,tooltip="Plays an audio chime when HUDs-Up detects the HUD.",key="audio_cb",font=options_font,p=default_padding),
    sg.Checkbox(text="Auto Close HUD",default=setting_auto_close,tooltip="Auto Closes the HUD when detected.",key="autoclose_cb",font=options_font,p=default_padding),    
    sg.Button(button_text="Update Options",size=(12,1),tooltip="Updates the options chosen.",font=options_font,p=default_padding),
    sg.Button(button_text="Update Apex Config",size=(20,1),tooltip="Appends the config file with the necessary lines to hide the HUD.",font=options_font,p=default_padding)],
    [sg.StatusBar("Stopped",size=(90,1),expand_x=True,expand_y=True,key='statusBar',text_color="Black",font=statusbar_font,justification="Right",relief="flat",background_color="#b9d4f1")]
]

visibility = bool(setting_enable_dev_console is not '')
output_console = [
    [sg.Output(text_color="Green",size=(90,5),p=default_padding,visible=visibility)]
]

layout = [
            [
            sg.Column(start_stop)
            ],
            [
            sg.HorizontalSeparator()
            ],
            [
            sg.Column(audio_autoclose)
            ],
            [
            sg.HorizontalSeparator()
            ],
            [
            sg.Column(output_console)
            ]
    ]

def main():
    # Appends the apex configuration file with the hide hud option
    def appendProfile():
        with open(apexProfile, "a") as cfgFile:
            cfgFile.write('\nbind "7" "+; gameui_hide"')

    # Determines where we should look for images. If none are found, it pulls from the root of its own directory.
    def findmyimage():
        if values["folder_selection"]:
            image_folder = str(values["folder_selection"])
        elif setting_image_folder:
            image_folder = setting_image_folder
        elif setting_image_folder == "" :
            image_folder = (os.getcwd().replace("\\","/"))
        return image_folder

    # Takes the values from the last known start/update option start
    def autosave():
        try:
            configParser['settings']['user_confidence'] = str(value_storage["confidence"])
            configParser['settings']['user_frequency'] = str(value_storage["frequency"])
            configParser['settings']['auto_close'] = str(value_storage["autoclose_cb"])
            configParser['settings']['chime_option'] = str(value_storage["audio_cb"])
            with open('settings.cfg','w') as configfile:
                configParser.write(configfile)
        except:
            print("Couldn't save user settings.")

    # Finding the image on screen
    def multi_image_recognition():
        print("HUDs up is now running.")
        window['statusBar'].Update("Running")
        while SHOULD_TERMINATE == False:
            for images in os.listdir(os.getcwd()):
                if images.endswith(".jpg"):
                    image_location = pyautogui.locateOnScreen(images,confidence=values["confidence"])
                    if image_location is not None:
                        print("HUD was detected.")
                        window['statusBar'].Update("HUD Detected")
                        if values["audio_cb"] == True:
                            winsound.PlaySound(alertsound, winsound.SND_FILENAME)
                        if values["autoclose_cb"] == True:
                            print("Closing HUD.")
                            window['statusBar'].Update("HUD Closed")
                            pydirectinput.keyDown('7')
                            pydirectinput.keyDown('esc')
                            pydirectinput.keyUp('esc')
                            pydirectinput.keyUp('7')
            pixelColorDetection()
            threading.Event().wait(values["frequency"])

    def pixelColorDetection():
    ## Health Bar Location is 179, 1017. Truecolor is (255, 255, 255) / Health Bar is consistent
    ## Map White Location is 53, 43. True color is 225,225,225 / map is consistent, but pixel is in gray if we care.
    ## Squads white location 1837, 76. Same true color / Squads is consistent
    ## Ult Grey Position 959, 912. True Color (186, 185, 184) / This is super inconsistent. 
    ## Direction Number Location 931, 110. True Color (210, 210, 210) / Not very consistent, but we could user 210 +/- 15, but this still might not be wide enough.
        pixelColor_healthBar = pyautogui.pixel(179, 1017)
        pixelColor_map = pyautogui.pixel(53, 43)
        pixelColor_squads = pyautogui.pixel(1837, 76)
        pixelColor_ultTopBar = pyautogui.pixel(959, 912)
        pixelColor_compassNumberBar = pyautogui.pixel(931, 110)
        print(pixelColor_healthBar)
        print(pixelColor_squads)
        print(pixelColor_map)
        print(pixelColor_ultTopBar)
        print(pixelColor_compassNumberBar)

    def startProcess():
        with open(apexProfile, 'r') as cfgFile:
            lastLine = cfgFile.readlines()[-1]
        if lastLine == 'bind "7" "+; gameui_hide"':
            print("Starting HUDs-UP with images in: " + image_folder_location + " and a confidence of " + str(values["confidence"]))
            window['statusBar'].Update("Starting")
            window["Start"].Update(disabled=True)        
            thread = threading.Thread(target=multi_image_recognition, daemon=True)
            thread.start()
            return thread
        else:
            sg.popup("The Apex configuration is not prepared for No Hud. Please manually update the config file or click 'Update CFG' to resolve this and try again. \n\nPress any key to continue.",title="Incorrect Apex Configuration",keep_on_top=True,background_color="#C14921",font=subheader_font,any_key_closes=True,button_type=5)

    # Main program loop
    window = sg.Window(title="HUDs-Up", layout=layout,size=default_window_size,icon=(menuicon),titlebar_icon=menuicon,margins=(0,0),element_padding=(0))
    while True:
        event, values = window.Read()
        if event == sg.WIN_CLOSED:
            autosave()
            break
        if event == "Start":
            image_folder_location = findmyimage()
            SHOULD_TERMINATE = False
            thread = startProcess()
        elif event == "Stop":
            SHOULD_TERMINATE = True
            print("Terminating HUDs Up.")
            value_storage = values
            autosave()
            try:
                thread.join()
                print("HUDs-Up Stopped.")
            except:
                print("Nothing to stop.")
            window["Start"].Update(disabled=False)
            window['statusBar'].Update("Stopped")
        elif event == "Update Options":
            print("Refreshing HUDs-Up.")
            SHOULD_TERMINATE = True
            try:
                thread.join()
            except:
                print("Nothing to refresh. Starting.")
            image_folder_location = findmyimage()
            SHOULD_TERMINATE = False
            startProcess()
        elif event == "Update Apex Config":
            appendProfile()
            window['statusBar'].Update("Apex Profile Updated.")

if __name__ == "__main__":
    main()