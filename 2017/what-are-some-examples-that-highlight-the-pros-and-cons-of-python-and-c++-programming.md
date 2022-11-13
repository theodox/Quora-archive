# What are some examples that highlight the pros and cons of Python and C++ programming?

	author: Steve Theodore
	written: 2017-04-19
	views: 946
	upvotes: 6
	quora url: /What-are-some-examples-that-highlight-the-pros-and-cons-of-Python-and-C++-programming/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Just to amplify [Aaron Mefford](https://www.quora.com/profile/Aaron-Mefford)’s example, here is what Bjarne Stroustrup — the godfather of C++ — uses an example of a simple C++ program for the same HTML link grabbing task without third party libraries (except [boost](http://www.boost.org/), which is quasi-standard).

    #include <string>
    #include <set>
    #include <iostream>
    #include <sstream>
    #include <regex>
    #include <boost/asio.hpp>
    
    using namespace std;
    
    set<string> get_strings(istream& is, regex pat)
    {
     set<string> res;
     smatch m;
     for (string s; getline(is, s);) // read a line
     if (regex_search(s, m, pat))
     res.insert(m[0]); // save match in set
     return res;
    }
    
    void connect_to_file(iostream& s, const string& server, const string& file)
    // open a connection to server and open an attach file to s
    // skip headers
    {
     if (!s)
     throw runtime_error{ "can't connect\n" };
    
     // Request to read the file from the server:
     s << "GET " << "http://" + server + "/" + file << " HTTP/1.0\r\n";
     s << "Host: " << server << "\r\n";
     s << "Accept: */*\r\n";
     s << "Connection: close\r\n\r\n";
    
     // Check that the response is OK:
     string http_version;
     unsigned int status_code;
     s >> http_version >> status_code;
    
     string status_message;
     getline(s, status_message);
     if (!s || http_version.substr(0, 5) != "HTTP/")
     throw runtime_error{ "Invalid response\n" };
    
     if (status_code != 200)
     throw runtime_error{ "Response returned with status code" };
    
     // Discard the response headers, which are terminated by a blank line:
     string header;
     while (getline(s, header) && header != "\r")
     ;
    }
    
    int main()
    {
     try {
     string server = "www.stroustrup.com";
     boost::asio::ip::tcp::iostream s{ server, "http" }; // make a connection
     connect_to_file(s, server, "C++.html"); // check and open file
    
     regex pat{ R"((http://)?www([./#\+-]\w*)+)" }; // URL
     for (auto x : get_strings(s, pat)) // look for URLs
     cout << x << '\n';
     }
     catch (std::exception& e) {
     std::cout << "Exception: " << e.what() << "\n";
     return 1;
     }
    }

Here’s the a completely vanilla Python version with only the standard library:

    import urllib2, re
    address = "http://www.stroustrup.com/C++.html"
    req = urllib2.urlopen(address)
    html = req.read()
    links = re.findall('"((http)s?://.*?)"', html)
    print links

It’s not an entirely fair comparison — as the other answer notes: you can use third party C++ libraries to write a similarly short program. However the wide availability of high quality libraries in every Python installation is part of Python’s core strength. C++ culture inclines much more toward the ‘roll your own’ aesthetic as well. So this is a pretty good apples-to-apples as far as code style, readability and native capacity.

Original - with amusingly dreary language fanboy arguments galore, [here](https://codegolf.stackexchange.com/questions/44278/debunking-stroustrups-debunking-of-the-myth-c-is-for-large-complicated-pro/44279#44279)

