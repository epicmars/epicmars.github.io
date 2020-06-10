var unsplash = {
    baseUrl: "https://api.unsplash.com/",
    accessKey: "d945a361e65ebf42cefda32bef69ea1fd2fa4029231cfc133d66dca73ab985b6"
}

/**
 * {
    "id": "Qdr4mpifNQQ",
    "created_at": "2018-03-19T07:45:24-04:00",
    "updated_at": "2018-05-09T05:15:55-04:00",
    "width": 5472,
    "height": 3648,
    "color": "#F3E3D2",
    "description": null,
    "urls": {
        "raw": "https://images.unsplash.com/photo-1521459893400-80c3a8926f5b?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjMyMDE3fQ&s=ec5ba2979d9ac3b4f372062c91ffff29",
        "full": "https://images.unsplash.com/photo-1521459893400-80c3a8926f5b?ixlib=rb-0.3.5&q=85&fm=jpg&crop=entropy&cs=srgb&ixid=eyJhcHBfaWQiOjMyMDE3fQ&s=b340b9e974abc2e62ef0f5423f7f3727",
        "regular": "https://images.unsplash.com/photo-1521459893400-80c3a8926f5b?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjMyMDE3fQ&s=600db1f8b9761decda8152d8eb1e20a2",
        "small": "https://images.unsplash.com/photo-1521459893400-80c3a8926f5b?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=400&fit=max&ixid=eyJhcHBfaWQiOjMyMDE3fQ&s=9441e5151b8a210c7312cd8feba8f824",
        "thumb": "https://images.unsplash.com/photo-1521459893400-80c3a8926f5b?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=200&fit=max&ixid=eyJhcHBfaWQiOjMyMDE3fQ&s=089fb3b7813b395520826fc4700cc652"
    },
    "links": {
        "self": "https://api.unsplash.com/photos/Qdr4mpifNQQ",
        "html": "https://unsplash.com/photos/Qdr4mpifNQQ",
        "download": "https://unsplash.com/photos/Qdr4mpifNQQ/download",
        "download_location": "https://api.unsplash.com/photos/Qdr4mpifNQQ/download"
    },
    "categories": [],
    "sponsored": false,
    "likes": 4,
    "liked_by_user": false,
    "current_user_collections": [],
    "slug": null,
    "user": {
        "id": "MOoBF6DIHSs",
        "updated_at": "2018-06-27T11:18:30-04:00",
        "username": "jamesbold",
        "name": "James Bold",
        "first_name": "James",
        "last_name": "Bold",
        "twitter_username": "iamjamesbold",
        "portfolio_url": "https://smartphotocourses.com",
        "bio": "Photography, writer, creator.",
        "location": null,
        "links": {
            "self": "https://api.unsplash.com/users/jamesbold",
            "html": "https://unsplash.com/@jamesbold",
            "photos": "https://api.unsplash.com/users/jamesbold/photos",
            "likes": "https://api.unsplash.com/users/jamesbold/likes",
            "portfolio": "https://api.unsplash.com/users/jamesbold/portfolio",
            "following": "https://api.unsplash.com/users/jamesbold/following",
            "followers": "https://api.unsplash.com/users/jamesbold/followers"
        },
        "profile_image": {
            "small": "https://images.unsplash.com/profile-1492679404723-7d73c381e4a5?ixlib=rb-0.3.5&q=80&fm=jpg&crop=faces&cs=tinysrgb&fit=crop&h=32&w=32&s=1e71bf8fbb0228779557cc76d074126a",
            "medium": "https://images.unsplash.com/profile-1492679404723-7d73c381e4a5?ixlib=rb-0.3.5&q=80&fm=jpg&crop=faces&cs=tinysrgb&fit=crop&h=64&w=64&s=274a3a90072b1a95ec7e241832abb4e8",
            "large": "https://images.unsplash.com/profile-1492679404723-7d73c381e4a5?ixlib=rb-0.3.5&q=80&fm=jpg&crop=faces&cs=tinysrgb&fit=crop&h=128&w=128&s=3d5f7851f2af9c02b21ca37fc40d2c5f"
        },
        "instagram_username": "michaelbold1",
        "total_collections": 0,
        "total_likes": 5,
        "total_photos": 64
    },
    "exif": {
        "make": null,
        "model": null,
        "exposure_time": null,
        "aperture": null,
        "focal_length": null,
        "iso": null
    },
    "views": 351967,
    "downloads": 784
}
 */
function randomUnsplashPhoto() {
    // get cached photo
    let photo = cachedPhoto();
    if (!isExpired(photo)) {
        loadPhoto(photo);
        return;
    }

    let requestURL = unsplash.baseUrl + "/photos/random";
    let request = new XMLHttpRequest();
    request.open("GET", requestURL, true);
    request.setRequestHeader("Accept-Version", "v1");
    request.setRequestHeader("Authorization", "Client-ID " + unsplash.accessKey);
    request.responseType = "json"
    request.onload = function () {
        photo = {
            timestamp : new Date(),
            data : request.response
        }
        loadPhoto(photo)
        savePhoto(photo)
        // console.log("response: " + JSON.stringify(photo))
    }
    request.send();
}

function isExpired(photo) {
    return null == photo || (Date.now() - Date.parse(photo.timestamp) > 15 * 60 * 1000);
}

function cachedPhoto() {
    let cachedPhoto = localStorage.getItem('unsplash-random');
    // console.log("cached: " + cachedPhoto)
    if (null == cachedPhoto) {
        return null;
    }
    try {
        return JSON.parse(cachedPhoto);
    } catch (e) {
        return null;
    }
}

function savePhoto(photo) {
    localStorage.setItem("unsplash-random", JSON.stringify(photo));
}

function loadPhoto(photo) {
    document.getElementById("unsplash-img").src = photo.data.urls.regular;
}

randomUnsplashPhoto();