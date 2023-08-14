import axios from "axios";

const quartierApi = {
    async getZones() {
        try {
          const response = await axios.get("zoneAffichages");
          return response.data;
        } catch (error) {
          // Handle error
          const _error = {
              status: null,
              error: error.message
          }
          if('response' in error && 'data' in error.response && 'detail' in error.response.data) {
              _error.error = error.response.data.detail
              _error.status = error.response.status
          }
          return _error
        }
      },
}

export {
    quartierApi,
}