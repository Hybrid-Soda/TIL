const loadingList = document.querySelector('.search-result--loadingList')
const searchInput = document.querySelector('.search-box__button')
const searchResult = document.querySelector('.search-result')
const sentinel = document.createElement('div')
let limit = 100
let page = 1

searchInput.addEventListener('click', fetchAlbums)

async function fetchAlbums(page=1, limit=10) {
  const keyword = document.querySelector('.search-box__input').value
  loadingList.style.display = 'block'

  const API_URI = 'http://ws.audioscrobbler.com/2.0/'
  const API_KEY = ''
  const params = {
    method: 'album.search',
    api_key: API_KEY,
    album: keyword,
    format: 'json',
    limit: limit,
    page: page,
  }
  const response = await axios.get(API_URI, {params})
  const albums = response.data.results.albummatches.album

  loadingList.style.display = 'none'
  createCards(albums)
}

function createCards(albums) {
  albums.forEach(album => {
    // createElement
    const artistName = document.createElement('h2')
    const albumName = document.createElement('p')
    const cardText = document.createElement('div')
    const cardImg = document.createElement('img')
    const card = document.createElement('div')

    // fillContents
    cardText.classList.add('search-result__text')
    card.classList.add('search-result__card')
    cardImg.src = album.image[1]['#text']
    artistName.innerText = album.artist
    albumName.innerText = album.name

    // appendTags
    cardText.append(artistName, albumName)
    card.append(cardImg, cardText)
    card.addEventListener('click', _ => window.location.href = album.url)
    searchResult.appendChild(card)
  })
  // appendSentinel
  searchResult.append(sentinel)
}

// Intersection change callbacks
const getMoreAlbums = (entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      page += 1
      fetchAlbums(page)
    }
  })
}
const observer = new IntersectionObserver(getMoreAlbums)
observer.observe(sentinel)