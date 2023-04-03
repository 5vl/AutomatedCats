// To use any npm package on Pipedream, just import it
import axios from "axios"
import Path from 'path'
import fs from 'fs'

export default defineComponent({
  async run({ steps, $ }) {
    let url = ""
    await axios.get("https://api.thecatapi.com/v1/images/search?mime_types=jpg,png&api_key=API_KEY").then((res) => {
      url = res.data[0].url
    })
    const path = Path.resolve('/tmp', 'cat.jpg')

    const { data } = await axios({
      method: 'GET',
      url,
      responseType: 'arraybuffer',
    })
    fs.writeFileSync(path, data)
    return url
  },
})
