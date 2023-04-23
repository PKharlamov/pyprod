import {defineStore} from "pinia";

export const useTreeStore = defineStore('tree', {
    state: () => ({
        isTreeVisible: false,
    }),
});