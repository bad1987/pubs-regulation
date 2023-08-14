import axios from "axios";
import { useQuartierStore } from "../stores/quartierStore";

const quartierApi = {
    async getZones(router) {
        axios.get("zoneAffichages")
        .then((response) => {
            useQuartierStore().SetZones(response.data);
        })
        .catch((error) => {
            console.log(error);
            if (error.response.status === 401) {
                router.push("/login");                
            }
            else if (error.response.status === 403) {
                router.push("/error/403");
            }
        })
    },
}

export {
    quartierApi,
}