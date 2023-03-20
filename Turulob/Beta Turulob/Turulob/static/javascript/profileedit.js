
const initSel = (elem, a, pl = "") => {
    elem.innerHTML += `<option value="">Select ${pl}</option>`
    for (i in a) {
        elem.innerHTML += `<option value="${a[i]}">${a[i]}</option>`
    }
}

{
    let country = document.querySelector("[name=locationCountry]")
    let state = document.querySelector("[name=locationState]")
    let city = document.querySelector("[name=locationCity")

    initSel(country, Object.keys(cscdata), "country")

    let initCity = () => {
        city.value = ""
        if (country.value != "" && state.value != "") {
            initSel(city, cscdata[country.value][state.value], "city")
        }
        else {
            initSel(city, [], country.value != "" ? "state first" : "country first")
            //city.value="" is used outside so if state changes, city becomes null too
        }
    }

    let initState = () => {
        state.value = ""

        if (country.value != "") {//country pata hai
            initSel(state, Object.keys(cscdata[country.value]), "state")
        }
        else {//country nai pata
            initSel(state, [], "country first")
            //state.value="" is used outside so if country changes, state becomes null too
        }
        initCity(); //
    }

    country.addEventListener("change", initState)
    state.addEventListener("change", initCity)
    initState()
    initCity()

}