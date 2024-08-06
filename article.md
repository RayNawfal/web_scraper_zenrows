# How to Scrape Products from a Web Page with infinite scroll via “Load more” button.

In this article, you’ll discover how to easily scrape product information for an e-commerce site using ZenRows’ powerful web scraping tools. With ZenRows, 
you can extract data from websites with minimal coding effort. Moreover, ZenRows offers not only API access but also SDKs, 
allowing integration with popular programming languages like Python and Javascript. ZenRows, by design, enables you to scrape data from multiple websites simultaneously while rotating proxies distribute the load across multiple IP addresses, 
making it virtually impossible for websites to detect and block scraping activities. <br/>

Whether you’re a data collector, analyst, or automation enthusiast, web scraping is an essential step forward in gaining data insights. With ZenRows, 
your web scraping abilities are elevated by its cutting-edge features, including bypassing anti-bot measures like CAPTCHAs, rotating proxies to avoid detection and IP blocking, 
and handling content that is generated dynamically by Javascript. This unique blend of features empowers you to extract valuable data with ease, 
making it a must-have tool for anyone who needs to automate their web scraping tasks.<br/>

Let’s imagine that you need to scrape data from an e-commerce website. The website by default displays the first 12 product items but you need to collect at least 48 non-duplicate items. 
The website provides a button that lets you load 12 more product items at a time. This step-by-step tutorial is specifically tailored for this task, 
helping you collect your data while simulating the click of a button. Let’s dive deep and start building your web scraping Python script.<br/>
 
## Step 1: Prerequisites

```bash
Python 3.12.4 (latest version recommended)
PIP (package installer for Python)
Python Integrated Development Environment (IDE) of you choice e.g (Pycharm, VS code)
```

Create a new Python file named scraper.py in your preferred directory. Open your terminal and navigate to the same directory to install ZenRows for web scraping and BeautifulSoup for HTML parsing using pip:

```bash
pip install zenrows # ZenRows Python SDK for web scraping
pip install beautifulsoup4 # To parse HTML 
```


**Note:** 
Make sure you’ve the latest version of pip installed by running before installing the packages<br/>
                ```bash
                Pip install -upgrade 
                ``` 
You can also install the packages using a virtual environment e.g.(conda, virtualenv) for better package management and isolation
If you encounter any issues during installation, ensure that your Python and pip versions are compatible with the packages you’re trying to install<br/>

If you’re interested in learning more about BeautifulSoup, check out Zenrows’s latest Blog post on How to Use a Proxy with BeautifulSoup<br/>

### Step 2: Get Access to the Content

In your `scraper.py` file, import the ZenRowsClient from the ZenRows library to make your first request. In this example, the /get endpoint from  https://www.scrapingcourse.com/button-click  will be used as the target site to test whether your script is functioning as expected.<br/> 

```py
from zenrows import ZenRowsClient

Url = "https://www.scrapingcourse.com/button-click"
client = ZenRowsClient("<YOUR_ZENROWS_API_KEY>")
Response = client.get(url)
# Print HTTP status code
print(response)
# Print result in text format 
print(response.text)
```

When making a request to a website you might encounter HTTP status codes that indicate whether the request was successful or not. By checking those codes you can ensure that your script is working correctly.

A similar result should be displayed on your console after running this script:


```html
<Response [200]>
<!DOCTYPE html>
<html lang="en"><head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Load More Button Challenge to Learn Web Scraping   - ScrapingCourse.com</title>

    <!-- Bootstrap CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async="" defer=""></script>
    <!-- Google tag (gtag.js) -->
    <script async="" src="https://www.googletagmanager.com/gtag/js?id=G-NZGD14H87G"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-NZGD14H87G');
    </script>
    <link rel="preload" as="style" href="https://www.scrapingcourse.com/build/assets/app-c2PwjGxE.css"><link rel="modulepreload" href="https://www.scrapingcourse.com/build/assets/app-D2jpX1vH.js"><link rel="stylesheet" href="https://www.scrapingcourse.com/build/assets/app-c2PwjGxE.css"><script type="module" src="https://www.scrapingcourse.com/build/assets/app-D2jpX1vH.js"></script>
</head>
<body data-new-gr-c-s-check-loaded="14.1174.0" data-gr-ext-installed="" itemscope="" itemtype="http://schema.org/WebPage">
    <header itemscope="" itemtype="http://schema.org/WPHeader">
        <!-- Navigation bar -->
        <nav id="main-navigation" class="navbar" data-testid="main-navigation" data-nav="main">
            <div class="container" id="nav-container" data-testid="nav-container" data-nav="container">
                <a href="/" class="logo-link flex items-center pt-4 pb-12" id="logo-link" data-testid="logo-link" data-nav="logo-link">
                    <img width="12" height="18" src="https://www.scrapingcourse.com/assets/images/logo.svg" class="logo-image inline-block" data-testid="logo-image" data-nav="logo-image">
                    <span class="brand-name font-bold text-lg leading-6 ml-2 highlight" data-testid="brand-name-1" data-nav="brand-name-1">Scraping</span>
                    <span class="brand-name text-lg leading-6 ml-1 highlight" data-testid="brand-name-2" data-nav="brand-name-2">Course</span>
                </a>
            </div>
        </nav>
    </header>

    <main class="page-content py-4" id="main-content" data-testid="main-content" data-content="main">
        <div class="container" id="content-container" data-testid="content-container" data-content="container">
            <div class="catalog" id="catalog" data-testid="catalog">

    <h1 id="page-title" class="page-title text-4xl font-bold mb-2 text-left gradient-text highlight gradient-text leading-10" data-testid="page-title" data-content="title">
    Load More
</h1>

<div class="challenge-info bg-[#EDF1FD] rounded-md p-4 mb-8 mt-5" id="challenge-info" data-testid="challenge-info" data-content="challenge-info">
    <div class="info-header flex items-center gap-2 pb-2" id="info-header" data-testid="info-header" data-content="info-header">
        <img width="25" height="15" src="https://www.scrapingcourse.com/assets/images/challenge.svg" data-testid="challenge-image" data-content="challenge-image">
        <h2 class="challenge-title text-xl font-bold" id="challenge-title" data-testid="challenge-title" data-content="challenge-title">Challenge</h2>
    </div>
    <p class="challenge-description flex" id="challenge-description" data-testid="challenge-description" data-content="challenge-description">
        Click 'Load More' button to load more products
    </p>
</div>

<div id="product-grid" class="product-grid grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4 mb-8" data-testid="product-grid">
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/chaz-kangeroo-hoodie">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh01-gray_main.jpg" alt="Chaz Kangeroo Hoodie">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Chaz Kangeroo Hoodie</span>
                <br>
                <span class="product-price text-slate-600">$52</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/teton-pullover-hoodie">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh02-black_main.jpg" alt="Teton Pullover Hoodie">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Teton Pullover Hoodie</span>
                <br>
                <span class="product-price text-slate-600">$70</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/bruno-compete-hoodie">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh03-black_main.jpg" alt="Bruno Compete Hoodie">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Bruno Compete Hoodie</span>
                <br>
                <span class="product-price text-slate-600">$63</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/frankie--sweatshirt">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh04-green_main.jpg" alt="Frankie  Sweatshirt">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Frankie  Sweatshirt</span>
                <br>
                <span class="product-price text-slate-600">$60</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/hollister-backyard-sweatshirt">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh05-white_main.jpg" alt="Hollister Backyard Sweatshirt">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Hollister Backyard Sweatshirt</span>
                <br>
                <span class="product-price text-slate-600">$52</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/stark-fundamental-hoodie">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh06-blue_main.jpg" alt="Stark Fundamental Hoodie">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Stark Fundamental Hoodie</span>
                <br>
                <span class="product-price text-slate-600">$42</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/hero-hoodie">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh07-gray_main.jpg" alt="Hero Hoodie">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Hero Hoodie</span>
                <br>
                <span class="product-price text-slate-600">$54</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/oslo-trek-hoodie">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh08-brown_main.jpg" alt="Oslo Trek Hoodie">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Oslo Trek Hoodie</span>
                <br>
                <span class="product-price text-slate-600">$42</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/abominable-hoodie">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh09-blue_main.jpg" alt="Abominable Hoodie">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Abominable Hoodie</span>
                <br>
                <span class="product-price text-slate-600">$69</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/mach-street-sweatshirt">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh10-blue_main.jpg" alt="Mach Street Sweatshirt">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Mach Street Sweatshirt</span>
                <br>
                <span class="product-price text-slate-600">$62</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/grayson-crewneck-sweatshirt">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh11-white_main.jpg" alt="Grayson Crewneck Sweatshirt">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Grayson Crewneck Sweatshirt</span>
                <br>
                <span class="product-price text-slate-600">$64</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/ajax-full-zip-sweatshirt">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh12-green_main.jpg" alt="Ajax Full-Zip Sweatshirt">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Ajax Full-Zip Sweatshirt</span>
                <br>
                <span class="product-price text-slate-600">$69</span>
            </div>
        </a>
    </div>
</div>

    <div class="flex justify-center" id="load-more-container" data-testid="load-more-container">
        <button id="load-more-btn" data-offset="10" class="bg-indigo-500 text-white px-6 py-2 rounded-md hover:bg-indigo-600 transition-colors" data-testid="load-more-btn">
          Load more
        </button>
    </div>
</div>

<script>
    document.getElementById('load-more-btn').addEventListener('click', function() {
        var button = this;
        var offset = button.getAttribute('data-offset');

        fetch(`/ajax/products?offset=${offset}`)
            .then(response => response.text()) // We're loading direct html instead of JSON data
            .then(html => {
                var container = document.getElementById('product-grid');
                container.insertAdjacentHTML('beforeend', html); // Append the HTML to the container

                button.setAttribute('data-offset', parseInt(offset) + 10);

                // Hide the button if no more items to load
                if (!html.trim()) {
                    button.style.display = 'none';
                }
            })
            .catch(error => console.error('Error loading more items:', error));
    });
</script>

        </div>
    </main>

    <!-- Bootstrap and jQuery libraries -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.2/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>


</body></html>
```



## Step 3: Load More Products 

After successfully receiving a response, this additional code will demonstrate how to load more products by simulating the click of the load more button to scrap at least 48 non-duplicate products. This is a common scenario in web scraping, where a website loads more content as you scroll or click a button. By using ZenRows’ JavaScript rendering capabilities, you can simulate the click of the load more button and extract the additional products. To do this, you’ll use the js_instructions parameter in your ZenRows request, which allows you to specify JavaScript instructions to be executed on the page.<br/>

```py
import urllib
import json
From zenrows import ZenRowsClient
From bs4 import BeautifulSoup

Url = 'https://www.scrapingcourse.com/button-click'
apikey = '<YOUR_ZENROWS_API_KEY>'
js_instructions = []

# Append Javascript functions to js_instructions array
# Simulate clicking "load more" button 4 times 
# for at least 48 non duplicate product results
for i in range(5):
    js_instructions.append({"wait": 3000},)
    js_instructions.append({"evaluate": "document.getElementById('load-more-btn').click();"},)

params = {
    'url': url,
    'apikey': apikey,
    'js_render':'true',
    'js_instructions':urllib.parse.quote(json.dumps(js_instructions))
}

client = ZenRowsClient("<YOUR_ZENROWS_API_KEY>")
Response = client.get(url, params=params)
# Print result in text format 
print(response.text)
```

A similar result should be displayed on your console after running this script:

```html
<html lang="en"><head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Load More Button Challenge to Learn Web Scraping   - ScrapingCourse.com</title>

    <!-- Bootstrap CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async="" defer=""></script>
    <!-- Google tag (gtag.js) -->
    <script async="" src="https://www.googletagmanager.com/gtag/js?id=G-NZGD14H87G"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-NZGD14H87G');
    </script>
    <link rel="preload" as="style" href="https://www.scrapingcourse.com/build/assets/app-c2PwjGxE.css"><link rel="modulepreload" href="https://www.scrapingcourse.com/build/assets/app-D2jpX1vH.js"><link rel="stylesheet" href="https://www.scrapingcourse.com/build/assets/app-c2PwjGxE.css"><script type="module" src="https://www.scrapingcourse.com/build/assets/app-D2jpX1vH.js"></script>
</head>
<body data-new-gr-c-s-check-loaded="14.1174.0" data-gr-ext-installed="" itemscope="" itemtype="http://schema.org/WebPage">
    <header itemscope="" itemtype="http://schema.org/WPHeader">
        <!-- Navigation bar -->
        <nav id="main-navigation" class="navbar" data-testid="main-navigation" data-nav="main">
            <div class="container" id="nav-container" data-testid="nav-container" data-nav="container">
                <a href="/" class="logo-link flex items-center pt-4 pb-12" id="logo-link" data-testid="logo-link" data-nav="logo-link">
                    <img width="12" height="18" src="https://www.scrapingcourse.com/assets/images/logo.svg" class="logo-image inline-block" data-testid="logo-image" data-nav="logo-image">
                    <span class="brand-name font-bold text-lg leading-6 ml-2 highlight" data-testid="brand-name-1" data-nav="brand-name-1">Scraping</span>
                    <span class="brand-name text-lg leading-6 ml-1 highlight" data-testid="brand-name-2" data-nav="brand-name-2">Course</span>
                </a>
            </div>
        </nav>
    </header>

    <main class="page-content py-4" id="main-content" data-testid="main-content" data-content="main">
        <div class="container" id="content-container" data-testid="content-container" data-content="container">
            <div class="catalog" id="catalog" data-testid="catalog">

    <h1 id="page-title" class="page-title text-4xl font-bold mb-2 text-left gradient-text highlight gradient-text leading-10" data-testid="page-title" data-content="title">
    Load More
</h1>

<div class="challenge-info bg-[#EDF1FD] rounded-md p-4 mb-8 mt-5" id="challenge-info" data-testid="challenge-info" data-content="challenge-info">
    <div class="info-header flex items-center gap-2 pb-2" id="info-header" data-testid="info-header" data-content="info-header">
        <img width="25" height="15" src="https://www.scrapingcourse.com/assets/images/challenge.svg" data-testid="challenge-image" data-content="challenge-image">
        <h2 class="challenge-title text-xl font-bold" id="challenge-title" data-testid="challenge-title" data-content="challenge-title">Challenge</h2>
    </div>
    <p class="challenge-description flex" id="challenge-description" data-testid="challenge-description" data-content="challenge-description">
        Click 'Load More' button to load more products
    </p>
</div>

<div id="product-grid" class="product-grid grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4 mb-8" data-testid="product-grid">
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/chaz-kangeroo-hoodie">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh01-gray_main.jpg" alt="Chaz Kangeroo Hoodie">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Chaz Kangeroo Hoodie</span>
                <br>
                <span class="product-price text-slate-600">$52</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/teton-pullover-hoodie">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh02-black_main.jpg" alt="Teton Pullover Hoodie">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Teton Pullover Hoodie</span>
                <br>
                <span class="product-price text-slate-600">$70</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/bruno-compete-hoodie">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh03-black_main.jpg" alt="Bruno Compete Hoodie">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Bruno Compete Hoodie</span>
                <br>
                <span class="product-price text-slate-600">$63</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/frankie--sweatshirt">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh04-green_main.jpg" alt="Frankie  Sweatshirt">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Frankie  Sweatshirt</span>
                <br>
                <span class="product-price text-slate-600">$60</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/hollister-backyard-sweatshirt">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh05-white_main.jpg" alt="Hollister Backyard Sweatshirt">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Hollister Backyard Sweatshirt</span>
                <br>
                <span class="product-price text-slate-600">$52</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/stark-fundamental-hoodie">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh06-blue_main.jpg" alt="Stark Fundamental Hoodie">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Stark Fundamental Hoodie</span>
                <br>
                <span class="product-price text-slate-600">$42</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/hero-hoodie">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh07-gray_main.jpg" alt="Hero Hoodie">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Hero Hoodie</span>
                <br>
                <span class="product-price text-slate-600">$54</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/oslo-trek-hoodie">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh08-brown_main.jpg" alt="Oslo Trek Hoodie">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Oslo Trek Hoodie</span>
                <br>
                <span class="product-price text-slate-600">$42</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/abominable-hoodie">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh09-blue_main.jpg" alt="Abominable Hoodie">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Abominable Hoodie</span>
                <br>
                <span class="product-price text-slate-600">$69</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/mach-street-sweatshirt">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh10-blue_main.jpg" alt="Mach Street Sweatshirt">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Mach Street Sweatshirt</span>
                <br>
                <span class="product-price text-slate-600">$62</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/grayson-crewneck-sweatshirt">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh11-white_main.jpg" alt="Grayson Crewneck Sweatshirt">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Grayson Crewneck Sweatshirt</span>
                <br>
                <span class="product-price text-slate-600">$64</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/ajax-full-zip-sweatshirt">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh12-green_main.jpg" alt="Ajax Full-Zip Sweatshirt">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Ajax Full-Zip Sweatshirt</span>
                <br>
                <span class="product-price text-slate-600">$69</span>
            </div>
        </a>
    </div>
<div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/grayson-crewneck-sweatshirt">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh11-white_main.jpg" alt="Grayson Crewneck Sweatshirt">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Grayson Crewneck Sweatshirt</span>
                <br>
                <span class="product-price text-slate-600">$64</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/ajax-full-zip-sweatshirt">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh12-green_main.jpg" alt="Ajax Full-Zip Sweatshirt">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Ajax Full-Zip Sweatshirt</span>
                <br>
                <span class="product-price text-slate-600">$69</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/marco-lightweight-active-hoodie">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh13-blue_main.jpg" alt="Marco Lightweight Active Hoodie">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Marco Lightweight Active Hoodie</span>
                <br>
                <span class="product-price text-slate-600">$74</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/beaumont-summit-kit">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mj01-yellow_main.jpg" alt="Beaumont Summit Kit">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Beaumont Summit Kit</span>
                <br>
                <span class="product-price text-slate-600">$42</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/hyperion-elements-jacket">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mj02-green_main.jpg" alt="Hyperion Elements Jacket">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Hyperion Elements Jacket</span>
                <br>
                <span class="product-price text-slate-600">$51</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/montana-wind-jacket">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mj03-black_main.jpg" alt="Montana Wind Jacket">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Montana Wind Jacket</span>
                <br>
                <span class="product-price text-slate-600">$49</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/kenobi-trail-jacket">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mj04-black_main.jpg" alt="Kenobi Trail Jacket">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Kenobi Trail Jacket</span>
                <br>
                <span class="product-price text-slate-600">$47</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/jupiter-all-weather-trainer">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mj06-blue_main.jpg" alt="Jupiter All-Weather Trainer">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Jupiter All-Weather Trainer</span>
                <br>
                <span class="product-price text-slate-600">$56.99</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/orion-two-tone-fitted-jacket">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mj07-red_main.jpg" alt="Orion Two-Tone Fitted Jacket">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Orion Two-Tone Fitted Jacket</span>
                <br>
                <span class="product-price text-slate-600">$72</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/lando-gym-jacket">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mj08-gray_main.jpg" alt="Lando Gym Jacket">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Lando Gym Jacket</span>
                <br>
                <span class="product-price text-slate-600">$99</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/taurus-elements-shell">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mj09-yellow_main.jpg" alt="Taurus Elements Shell">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Taurus Elements Shell</span>
                <br>
                <span class="product-price text-slate-600">$65</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/mars-heattech&amp;trade;-pullover">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mj10-red_main.jpg" alt="Mars HeatTech&amp;trade; Pullover">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Mars HeatTech&amp;trade; Pullover</span>
                <br>
                <span class="product-price text-slate-600">$66</span>
            </div>
        </a>
    </div>
<div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/taurus-elements-shell">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mj09-yellow_main.jpg" alt="Taurus Elements Shell">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Taurus Elements Shell</span>
                <br>
                <span class="product-price text-slate-600">$65</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/mars-heattech&amp;trade;-pullover">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mj10-red_main.jpg" alt="Mars HeatTech&amp;trade; Pullover">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Mars HeatTech&amp;trade; Pullover</span>
                <br>
                <span class="product-price text-slate-600">$66</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/typhon-performance-fleece-lined-jacket">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mj11-black_main.jpg" alt="Typhon Performance Fleece-lined Jacket">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Typhon Performance Fleece-lined Jacket</span>
                <br>
                <span class="product-price text-slate-600">$60</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/proteus-fitness-jackshirt">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mj12-orange_main.jpg" alt="Proteus Fitness Jackshirt">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Proteus Fitness Jackshirt</span>
                <br>
                <span class="product-price text-slate-600">$45</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/caesar-warm-up-pant">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mp01-gray_main.jpg" alt="Caesar Warm-Up Pant">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Caesar Warm-Up Pant</span>
                <br>
                <span class="product-price text-slate-600">$35</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/viktor-lumatech&amp;trade;-pant">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mp02-gray_main.jpg" alt="Viktor LumaTech&amp;trade; Pant">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Viktor LumaTech&amp;trade; Pant</span>
                <br>
                <span class="product-price text-slate-600">$46</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/geo-insulated-jogging-pant">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mp03-black_main.jpg" alt="Geo Insulated Jogging Pant">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Geo Insulated Jogging Pant</span>
                <br>
                <span class="product-price text-slate-600">$51</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/supernova-sport-pant">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mp04-gray_main.jpg" alt="Supernova Sport Pant">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Supernova Sport Pant</span>
                <br>
                <span class="product-price text-slate-600">$45</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/kratos-gym-pant">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mp05-blue_main.jpg" alt="Kratos Gym Pant">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Kratos Gym Pant</span>
                <br>
                <span class="product-price text-slate-600">$57</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/mithra-warmup-pant">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mp06-gray_main.jpg" alt="Mithra Warmup Pant">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Mithra Warmup Pant</span>
                <br>
                <span class="product-price text-slate-600">$28</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/thorpe-track-pant">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mp07-blue_main.jpg" alt="Thorpe Track Pant">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Thorpe Track Pant</span>
                <br>
                <span class="product-price text-slate-600">$68</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/zeppelin-yoga-pant">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mp08-green_main.jpg" alt="Zeppelin Yoga Pant">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Zeppelin Yoga Pant</span>
                <br>
                <span class="product-price text-slate-600">$82</span>
            </div>
        </a>
    </div>
<div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/thorpe-track-pant">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mp07-blue_main.jpg" alt="Thorpe Track Pant">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Thorpe Track Pant</span>
                <br>
                <span class="product-price text-slate-600">$68</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/zeppelin-yoga-pant">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mp08-green_main.jpg" alt="Zeppelin Yoga Pant">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Zeppelin Yoga Pant</span>
                <br>
                <span class="product-price text-slate-600">$82</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/livingston-all-purpose-tight">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mp09-blue_main.jpg" alt="Livingston All-Purpose Tight">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Livingston All-Purpose Tight</span>
                <br>
                <span class="product-price text-slate-600">$75</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/orestes-yoga-pant">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mp10-black_main.jpg" alt="Orestes Yoga Pant">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Orestes Yoga Pant</span>
                <br>
                <span class="product-price text-slate-600">$66</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/aether-gym-pant">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mp11-brown_main.jpg" alt="Aether Gym Pant">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Aether Gym Pant</span>
                <br>
                <span class="product-price text-slate-600">$74</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/cronus-yoga-pant">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mp12-black_main.jpg" alt="Cronus Yoga Pant">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Cronus Yoga Pant</span>
                <br>
                <span class="product-price text-slate-600">$48</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/aero-daily-fitness-tee">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/ms01-blue_main.jpg" alt="Aero Daily Fitness Tee">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Aero Daily Fitness Tee</span>
                <br>
                <span class="product-price text-slate-600">$24</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/ryker-lumatech&amp;trade;-tee-(v-neck)">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/ms02-gray_main.jpg" alt="Ryker LumaTech&amp;trade; Tee (V-neck)">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Ryker LumaTech&amp;trade; Tee (V-neck)</span>
                <br>
                <span class="product-price text-slate-600">$28</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/balboa-persistence-tee">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/ms03-black_main.jpg" alt="Balboa Persistence Tee">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Balboa Persistence Tee</span>
                <br>
                <span class="product-price text-slate-600">$29</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/gobi-heattec&amp;reg;-tee">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/ms04-orange_main.jpg" alt="Gobi HeatTec&amp;reg; Tee">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Gobi HeatTec&amp;reg; Tee</span>
                <br>
                <span class="product-price text-slate-600">$29</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/helios-evercool&amp;trade;-tee">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/ms05-blue_main.jpg" alt="Helios EverCool&amp;trade; Tee">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Helios EverCool&amp;trade; Tee</span>
                <br>
                <span class="product-price text-slate-600">$24</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/zoltan-gym-tee">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/ms06-blue_main.jpg" alt="Zoltan Gym Tee">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Zoltan Gym Tee</span>
                <br>
                <span class="product-price text-slate-600">$29</span>
            </div>
        </a>
    </div>
<div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/helios-evercool&amp;trade;-tee">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/ms05-blue_main.jpg" alt="Helios EverCool&amp;trade; Tee">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Helios EverCool&amp;trade; Tee</span>
                <br>
                <span class="product-price text-slate-600">$24</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/zoltan-gym-tee">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/ms06-blue_main.jpg" alt="Zoltan Gym Tee">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Zoltan Gym Tee</span>
                <br>
                <span class="product-price text-slate-600">$29</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/deion-long-sleeve-evercool&amp;trade;-tee">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/ms07-green_main.jpg" alt="Deion Long-Sleeve EverCool&amp;trade; Tee">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Deion Long-Sleeve EverCool&amp;trade; Tee</span>
                <br>
                <span class="product-price text-slate-600">$39</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/strike-endurance-tee">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/ms08-black_main.jpg" alt="Strike Endurance Tee">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Strike Endurance Tee</span>
                <br>
                <span class="product-price text-slate-600">$39</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/ryker-lumatech&amp;trade;-tee-(crew-neck)">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/ms09-blue_main.jpg" alt="Ryker LumaTech&amp;trade; Tee (Crew-neck)">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Ryker LumaTech&amp;trade; Tee (Crew-neck)</span>
                <br>
                <span class="product-price text-slate-600">$32</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/logan--heattec&amp;reg;-tee">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/ms10-blue_main.jpg" alt="Logan  HeatTec&amp;reg; Tee">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Logan  HeatTec&amp;reg; Tee</span>
                <br>
                <span class="product-price text-slate-600">$24</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/atomic-endurance-running-tee-(v-neck)">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/ms11-green_main.jpg" alt="Atomic Endurance Running Tee (V-neck)">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Atomic Endurance Running Tee (V-neck)</span>
                <br>
                <span class="product-price text-slate-600">$28</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/atomic-endurance-running-tee-(crew-neck)">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/ms12-red_main.jpg" alt="Atomic Endurance Running Tee (Crew-Neck)">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Atomic Endurance Running Tee (Crew-Neck)</span>
                <br>
                <span class="product-price text-slate-600">$29</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/cobalt-cooltech&amp;trade;-fitness-short">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/msh01-blue_main.jpg" alt="Cobalt CoolTech&amp;trade; Fitness Short">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Cobalt CoolTech&amp;trade; Fitness Short</span>
                <br>
                <span class="product-price text-slate-600">$44</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/apollo-running-short">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/msh02-black_main.jpg" alt="Apollo Running Short">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Apollo Running Short</span>
                <br>
                <span class="product-price text-slate-600">$32.5</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/meteor-workout-short">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/msh03-blue_main.jpg" alt="Meteor Workout Short">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Meteor Workout Short</span>
                <br>
                <span class="product-price text-slate-600">$32.5</span>
            </div>
        </a>
    </div>
    <div class="product-item flex flex-col items-center rounded-lg">

        <a href="https://scrapingcourse.com/ecommerce/product/torque-power-short">
                        <img class="product-image rounded-lg" width="200" height="240" decoding="async" fetchpriority="high" src="https://scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/msh04-gray_main.jpg" alt="Torque Power Short">
            <div class="product-info self-start text-left w-full">
                <span class="product-name">Torque Power Short</span>
                <br>
                <span class="product-price text-slate-600">$32.5</span>
            </div>
        </a>
    </div>
</div>

    <div class="flex justify-center" id="load-more-container" data-testid="load-more-container">
        <button id="load-more-btn" data-offset="50" class="bg-indigo-500 text-white px-6 py-2 rounded-md hover:bg-indigo-600 transition-colors" data-testid="load-more-btn">
          Load more
        </button>
    </div>
</div>

<script>
    document.getElementById('load-more-btn').addEventListener('click', function() {
        var button = this;
        var offset = button.getAttribute('data-offset');

        fetch(`/ajax/products?offset=${offset}`)
            .then(response => response.text()) // We're loading direct html instead of JSON data
            .then(html => {
                var container = document.getElementById('product-grid');
                container.insertAdjacentHTML('beforeend', html); // Append the HTML to the container

                button.setAttribute('data-offset', parseInt(offset) + 10);

                // Hide the button if no more items to load
                if (!html.trim()) {
                    button.style.display = 'none';
                }
            })
            .catch(error => console.error('Error loading more items:', error));
    });
</script>

        </div>
    </main>

    <!-- Bootstrap and jQuery libraries -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.2/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>


</body></html>
```


## Step 4: Parse Product information

Now that you’ve run your code, it is time to parse the HTML and store the filtered data in a nested list. This is a crucial step that allows you to extract specific data you’re interested in and store it in a format that’s easy to work with. To parse the HTML, you’ll need to use BeautifulSoup library to extract the product name, product price and URL of the first 48 non-duplicate products.

```py
import urllib
import json
from zenrows import ZenRowsClient
from bs4 import BeautifulSoup

Url = 'https://www.scrapingcourse.com/button-click'
apikey = '<YOUR_ZENROWS_API_KEY>'
js_instructions = []

# Append Javascript functions to js_instructions array
# Simulate clicking "load more" button 3 times for 48 product result display
for i in range(5):
    js_instructions.append({"wait": 3000},)
    js_instructions.append({"evaluate": "document.getElementById('load-more-btn').click();"},)

params = {
    'url': url,
    'apikey': apikey,
    'js_render':'true',
    'js_instructions':urllib.parse.quote(json.dumps(js_instructions))
}

client = ZenRowsClient("<YOUR_ZENROWS_API_KEY>")
Response = client.get(url, params=params)
# Store data of each product
products = []
soup = BeautifulSoup(response.text, "html.parser")
# Loop through occurrences with an attribute "product-item"
for item in soup.find_all("div", attrs={"class", "product-item"}):
    href = item.contents[1].get("href")
    product_name = item.contents[1].find(class_='product-name').text
    product_price = item.contents[1].find(class_='product-price').text.replace('$', '')
    products.append([product_name, product_price, href])
# Sort the list according to the highest price
Products = sorted(products, key=lambda x:float(x[1], reverse=True
print(products)
```

A similar result should be displayed on your console after running this script:
```bash
[['Lando Gym Jacket', '99', 'https://scrapingcourse.com/ecommerce/product/lando-gym-jacket'], ['Zeppelin Yoga Pant', '82', 'https://scrapingcourse.com/ecommerce/product/zeppelin-yoga-pant'], ['Zeppelin Yoga Pant', '82', 'https://scrapingcourse.com/ecommerce/product/zeppelin-yoga-pant'], ['Livingston All-Purpose Tight', '75', 'https://scrapingcourse.com/ecommerce/product/livingston-all-purpose-tight'], ['Marco Lightweight Active Hoodie', '74', 'https://scrapingcourse.com/ecommerce/product/marco-lightweight-active-hoodie'], ['Aether Gym Pant', '74', 'https://scrapingcourse.com/ecommerce/product/aether-gym-pant'], ['Orion Two-Tone Fitted Jacket', '72', 'https://scrapingcourse.com/ecommerce/product/orion-two-tone-fitted-jacket'], ['Teton Pullover Hoodie', '70', 'https://scrapingcourse.com/ecommerce/product/teton-pullover-hoodie'], ['Abominable Hoodie', '69', 'https://scrapingcourse.com/ecommerce/product/abominable-hoodie'], ['Ajax Full-Zip Sweatshirt', '69', 'https://scrapingcourse.com/ecommerce/product/ajax-full-zip-sweatshirt'], ['Ajax Full-Zip Sweatshirt', '69', 'https://scrapingcourse.com/ecommerce/product/ajax-full-zip-sweatshirt'], ['Thorpe Track Pant', '68', 'https://scrapingcourse.com/ecommerce/product/thorpe-track-pant'], ['Thorpe Track Pant', '68', 'https://scrapingcourse.com/ecommerce/product/thorpe-track-pant'], ['Mars HeatTech&trade; Pullover', '66', 'https://scrapingcourse.com/ecommerce/product/mars-heattech&trade;-pullover'], ['Mars HeatTech&trade; Pullover', '66', 'https://scrapingcourse.com/ecommerce/product/mars-heattech&trade;-pullover'], ['Orestes Yoga Pant', '66', 'https://scrapingcourse.com/ecommerce/product/orestes-yoga-pant'], ['Taurus Elements Shell', '65', 'https://scrapingcourse.com/ecommerce/product/taurus-elements-shell'], ['Taurus Elements Shell', '65', 'https://scrapingcourse.com/ecommerce/product/taurus-elements-shell'], ['Grayson Crewneck Sweatshirt', '64', 'https://scrapingcourse.com/ecommerce/product/grayson-crewneck-sweatshirt'], ['Grayson Crewneck Sweatshirt', '64', 'https://scrapingcourse.com/ecommerce/product/grayson-crewneck-sweatshirt'], ['Bruno Compete Hoodie', '63', 'https://scrapingcourse.com/ecommerce/product/bruno-compete-hoodie'], ['Mach Street Sweatshirt', '62', 'https://scrapingcourse.com/ecommerce/product/mach-street-sweatshirt'], ['Frankie  Sweatshirt', '60', 'https://scrapingcourse.com/ecommerce/product/frankie--sweatshirt'], ['Typhon Performance Fleece-lined Jacket', '60', 'https://scrapingcourse.com/ecommerce/product/typhon-performance-fleece-lined-jacket'], ['Kratos Gym Pant', '57', 'https://scrapingcourse.com/ecommerce/product/kratos-gym-pant'], ['Jupiter All-Weather Trainer', '56.99', 'https://scrapingcourse.com/ecommerce/product/jupiter-all-weather-trainer'], ['Hero Hoodie', '54', 'https://scrapingcourse.com/ecommerce/product/hero-hoodie'], ['Chaz Kangeroo Hoodie', '52', 'https://scrapingcourse.com/ecommerce/product/chaz-kangeroo-hoodie'], ['Hollister Backyard Sweatshirt', '52', 'https://scrapingcourse.com/ecommerce/product/hollister-backyard-sweatshirt'], ['Hyperion Elements Jacket', '51', 'https://scrapingcourse.com/ecommerce/product/hyperion-elements-jacket'], ['Geo Insulated Jogging Pant', '51', 'https://scrapingcourse.com/ecommerce/product/geo-insulated-jogging-pant'], ['Montana Wind Jacket', '49', 'https://scrapingcourse.com/ecommerce/product/montana-wind-jacket'], ['Cronus Yoga Pant', '48', 'https://scrapingcourse.com/ecommerce/product/cronus-yoga-pant'], ['Kenobi Trail Jacket', '47', 'https://scrapingcourse.com/ecommerce/product/kenobi-trail-jacket'], ['Viktor LumaTech&trade; Pant', '46', 'https://scrapingcourse.com/ecommerce/product/viktor-lumatech&trade;-pant'], ['Proteus Fitness Jackshirt', '45', 'https://scrapingcourse.com/ecommerce/product/proteus-fitness-jackshirt'], ['Supernova Sport Pant', '45', 'https://scrapingcourse.com/ecommerce/product/supernova-sport-pant'], ['Stark Fundamental Hoodie', '42', 'https://scrapingcourse.com/ecommerce/product/stark-fundamental-hoodie'], ['Oslo Trek Hoodie', '42', 'https://scrapingcourse.com/ecommerce/product/oslo-trek-hoodie'], ['Beaumont Summit Kit', '42', 'https://scrapingcourse.com/ecommerce/product/beaumont-summit-kit'], ['Caesar Warm-Up Pant', '35', 'https://scrapingcourse.com/ecommerce/product/caesar-warm-up-pant'], ['Balboa Persistence Tee', '29', 'https://scrapingcourse.com/ecommerce/product/balboa-persistence-tee'], ['Gobi HeatTec&reg; Tee', '29', 'https://scrapingcourse.com/ecommerce/product/gobi-heattec&reg;-tee'], ['Zoltan Gym Tee', '29', 'https://scrapingcourse.com/ecommerce/product/zoltan-gym-tee'], ['Mithra Warmup Pant', '28', 'https://scrapingcourse.com/ecommerce/product/mithra-warmup-pant'], ['Ryker LumaTech&trade; Tee (V-neck)', '28', 'https://scrapingcourse.com/ecommerce/product/ryker-lumatech&trade;-tee-(v-neck)'], ['Aero Daily Fitness Tee', '24', 'https://scrapingcourse.com/ecommerce/product/aero-daily-fitness-tee'], ['Helios EverCool&trade; Tee', '24', 'https://scrapingcourse.com/ecommerce/product/helios-evercool&trade;-tee']]

```

## Step 5: Export Product Information to CSV

Let’s export the scraped data to a CSV file, a format that is easily readable and compatible with most data analysis tools. To do this, you’ll need to add the csv package to your list of imported libraries. With this package, you can open a CSV file, create field names (Product Name, Price, Link), and insert the data into rows allowing you to easily manipulate and format your data for future analysis as shown below.

```py
import csv
import urllib
import json 
from zenrows import ZenRowsClient
from bs4 import BeautifulSoup

Url = 'https://www.scrapingcourse.com/button-click'
apikey = '<YOUR_ZENROWS_API_KEY>'
js_instructions = []

# Append Javascript functions to js_instructions array
# Simulate clicking "load more" button 3 times for 48 product result display
for i in range(5):
    js_instructions.append({"wait": 3000},)
    js_instructions.append({"evaluate": "document.getElementById('load-more-btn').click();"},)

params = {
    'url': url,
    'apikey': apikey,
    'js_render':'true',
    'js_instructions':urllib.parse.quote(json.dumps(js_instructions))
}

client = ZenRowsClient("<YOUR_ZENROWS_API_KEY>")
Response = client.get(url, params=params)
# Store data of each product
products = []
soup = BeautifulSoup(response.text, "html.parser")
# Loop through occurrences with an attribute "product-item"
for item in soup.find_all("div", attrs={"class", "product-item"}):
    href = item.contents[1].get("href")
    product_name = item.contents[1].find(class_='product-name').text
    product_price = item.contents[1].find(class_='product-price').text.replace('$', '')
    products.append([product_name, product_price, href])
# Sort the list according to the highest price
Products = sorted(products, key=lambda x:float(x[1], reverse=True

# Specify the file name for the CSV file
file_name = "products.csv"

# Field names (headers)
field_names = ["Product Name", "Price", "Link"]

# Open the file in write mode
with open(file_name, 'w', newline='') as file:
    writer = csv.writer(file) 
    writer.writerow(field_names)
    # Save first non duplicate 48 products
    for data in products[:48]:
        # Write the data to the CSV file
        writer.writerow(data)

print(f"Data successfully exported to CSV file '{file_name}'.")
```

Here is a snippet of the CSV file content.



### Step 6: Add Proxy Rotation

(Optional) Premium proxies at ZenRows provide enhanced performance, security, and anonymity for your web scraping activities. In addition, premium proxies are designed to handle large-scale scraping tasks, allowing you to perform a high volume of requests without being blocked. Here is the rewritten code with the included premium_proxy parameter, demonstrating how to use premium proxies.

```py 
import csv
import urllib
import json 
from zenrows import ZenRowsClient
from bs4 import BeautifulSoup

Url = 'https://www.scrapingcourse.com/button-click'
apikey = '<YOUR_ZENROWS_API_KEY>'
js_instructions = []

# Append Javascript functions to js_instructions array
# Simulate clicking "load more" button 3 times for 48 product result display
for i in range(5):
    js_instructions.append({"wait": 3000},)
    js_instructions.append({"evaluate": "document.getElementById('load-more-btn').click();"},)

params = {
    'url': url,
    'apikey': apikey,
    'js_render':'true',
    'js_instructions':urllib.parse.quote(json.dumps(js_instructions)),
    'Premium_proxy': 'true' # provide anonymity layer to web scraping activity
}

client = ZenRowsClient("<YOUR_ZENROWS_API_KEY>")
Response = client.get(url, params=params)
# store data of each product
products = []
soup = BeautifulSoup(response.text, "html.parser")
# Loop through occurrences with an attribute "product-item"
for item in soup.find_all("div", attrs={"class", "product-item"}):
    href = item.contents[1].get("href")
    product_name = item.contents[1].find(class_='product-name').text
    product_price = item.contents[1].find(class_='product-price').text.replace('$', '')
    products.append([product_name, product_price, href])
# Sort the list according to the highest price
Products = sorted(products, key=lambda x:float(x[1], reverse=True

# Specify the file name for the CSV file
file_name = "products.csv"

# Field names (headers)
field_names = ["Product Name", "Price", "Link"]

# Open the file in write mode
with open(file_name, 'w', newline='') as file:
    writer = csv.writer(file) 
    writer.writerow(field_names)
    # Save first non duplicate 48 products
    for data in products[:48]:
        # Write the data to the CSV file
        writer.writerow(data)

print(f"Data successfully exported to CSV file '{file_name}'.")

```

With ZenRows premium proxies, you can rest assured that your scraping activities will remain undetected and efficient. Whether you’re scraping data from e-commerce sites, social media platforms, or other online sources, ZenRows premium proxies provide the reliability and scalability you need to achieve your web scraping goals. If you’d like to know more about rotating proxies visit ZenRows Blog post on How to Rotate Proxies in Python.


## Step 7: Get Extra Data from Top Products

As a final step, you’ll extract additional data on the top 5 most expensive products, including their SKU and description. You’ll use the previously run code as a starting point and add additional logic to simulate clicks on each product, retrieve the extra product data, and then save the result to a new CSV file.

```py 
import csv
import urllib
import json 
from zenrows import ZenRowsClient
from bs4 import BeautifulSoup

Url = 'https://www.scrapingcourse.com/button-click'
apikey = '<YOUR_ZENROWS_API_KEY>'
js_instructions = []

# Append Javascript functions to js_instructions array
# Simulate clicking "load more" button 3 times for 48 product result display
for i in range(5):
    js_instructions.append({"wait": 3000},)
    js_instructions.append({"evaluate": "document.getElementById('load-more-btn').click();"},)

params = {
    'url': url,
    'apikey': apikey,
    'js_render':'true',
    'js_instructions':urllib.parse.quote(json.dumps(js_instructions)),
    'Premium_proxy': 'true' # provide anonymity layer to web scraping activity
}

client = ZenRowsClient("<YOUR_ZENROWS_API_KEY>")
Response = client.get(url, params=params)
# store data of each product
products = []
soup = BeautifulSoup(response.text, "html.parser")
# Loop through occurrences with an attribute "product-item"
for item in soup.find_all("div", attrs={"class", "product-item"}):
    href = item.contents[1].get("href")
    product_name = item.contents[1].find(class_='product-name').text
    product_price = item.contents[1].find(class_='product-price').text.replace('$', '')
    products.append([product_name, product_price, href])
# Sort the list according to the highest price
Products = sorted(products, key=lambda x:float(x[1], reverse=True

# Specify the file name for the CSV file
file_name = "products.csv"

# Field names (headers)
field_names = ["Product Name", "Price", "Link"]

# Open the file in write mode
with open(file_name, 'w', newline='') as file:
    writer = csv.writer(file) 
    writer.writerow(field_names)
    # Save first non duplicate 48 products
    for data in products[:48]:
        # Write the data to the CSV file
        writer.writerow(data)

print(f"Data successfully exported to CSV file '{file_name}'.")
 
params = {
    'url': url,
    'apikey': apikey,
    'js_render':'true'
}

# Loop through the first 5 items in the Products list
for product in products[:5]:
    url = product[2]
    response = client.get(url, params=params)
    soup = BeautifulSoup(response.text, "html.parser")
    for item in soup.find_all('div', attrs={'class': 'product_meta'}):
        sku = item.contents[1].find(class_='sku').text

    description = soup.select('.woocommerce-Tabs-panel')[0]
    desc = description.contents[3].text
    # Append to the already existing products list
    products[products.index(product)].extend([sku, desc])
# New csv file
file_name = "products_extra_data.csv"

# Field names (headers)
field_names = ["Product Name", "Price", "Link", "SKU", "Description"]

# Open the file in write mode
with open(file_name, 'w', newline='') as file:
    writer = csv.writer(file) 
    writer.writerow(field_names)
    # Save the first non duplicate 48 products
    for word in products[:48]:
        # Write the data to the CSV file
        writer.writerow(word)

print(f"CSV file '{file_name}' created successfully.")
```

Here is a snippet of the csv file content after extracting the new additional data

## Conclusion

In this tutorial, you learned to use ZenRows SDK for scraping product information from an e-commerce website. From installing the ZenRows library and importing the necessary dependencies to parsing HTML and storing data in a nested list, we have demonstrated the ease and power of using ZenRows as a solution for web scraping. By following these steps, you’ve learned how to simulate button clicks, bypass anti-bot measures, and extract valuable data with ease. With ZenRows, you can efficiently scrape data for multiple websites simultaneously, rotate proxies to avoid detection and render JavaScript content to extract even more data. 

If you’re interested in learning more about how to bypass CAPTCHAs and other anti-bot measures, check out the latest article on How to Avoid CAPTCHA and reCAPTCHA. For more advanced users, the ZenRows documentation provides detailed information on the API and SDKs’ functionalities.

