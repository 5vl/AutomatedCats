// To use any npm package, just import it
import axios from "axios"
import qs from "qs"

export default defineComponent({
  props: {
    store: {
      type: "data_store",
    },
  },
  async run({ steps, $ }) {
    const currTime = Date.now()
    const oldTime = await await this.store.get("time")
    if (currTime < oldTime) {
      const token = await this.store.get("access_token")
      return token
    }
    const refresh_token = await this.store.get("refresh_token")
    let data = await axios.post("https://api.twitter.com/2/oauth2/token", qs.stringify({
        "refresh_token": refresh_token,
        "grant_type": "refresh_token",
        "client_id": "CLIENT_ID"
        }),
        {
          headers: { 
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Basic BASIC_TOKEN"
          }
        }
      )
    data = data.data
    await this.store.set("refresh_token", data.refresh_token)
    await this.store.set("access_token", data.access_token)
    await this.store.set("time", currTime + 3600000)
    return data.access_token
  },
})
