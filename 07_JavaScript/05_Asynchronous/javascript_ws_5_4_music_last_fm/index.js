/* 
  아래에 코드를 작성해주세요.
*/
const keyword = document.querySelector('.search-box__input')
const searchBtn = document.querySelector('.search-box__button')
const API_URI = 'http://ws.audioscrobbler.com/2.0/'
const API_KEY = ''

const fetchAlbums = (page=1, limit=10) => {
  axios({
    method: 'get',
    url: API_URI,
    params: {
      method: 'album.search',
      limit: limit,
      page: page,
      album: keyword.value,
      api_key: API_KEY,
      format: 'json',
    }
  })
    .then((response) => {
      const albums = response.data.results.albummatches.album
      albums.forEach(elem => {
        // div 태그 만들고 클래스 부여하기
        const result = document.querySelector('.search-result')
        const link = document.createElement('a')
        const card = document.createElement('div')
        const cardImg = document.createElement('img')
        const text = document.createElement('div')
        const artist = document.createElement('h2')
        const album = document.createElement('p')

        link.href = elem.url
        link.style.textDecoration = 'none'
        link.style.color = 'black'
        card.classList.add('search-result__card')
        text.classList.add('search-result__text')
        cardImg.src = elem.image[1]['#text']
        artist.textContent = elem.artist
        album.textContent = elem.name

        text.appendChild(artist)
        text.appendChild(album)
        card.appendChild(cardImg)
        card.appendChild(text)
        result.appendChild(link)
        link.appendChild(card)
      })
    })
    .catch((error) => {
      alert('잠시 후 다시 시도해주세요')
    })
}
searchBtn.addEventListener('click', fetchAlbums)
