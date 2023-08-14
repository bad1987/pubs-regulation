import { defineStore } from "pinia";

export const useQuartierStore = defineStore("quartier", {
    state: () => ({
        zones: [],
        quartiers: []
    }),
    actions: {
        SetZones(zones) {
            this.zones = zones
        },
        SetQuartiers(quartiers) {
            this.quartiers = quartiers
        },
        getZones() {
            return this.zones
        },
        getQuartiers() {
            return this.quartiers
        }
    }
})