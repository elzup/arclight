import { clock } from './clock'
import { Lamp, Area } from './types'
const NUMS = 300

const config: { areas: Area[] } = {
  areas: [
    {
      name: 'swarippa',
      startAddress: 0,
      range: 30,
      func: clock,
    },
    {
      name: 'clock',
      startAddress: 30,
      range: 5 * 8,
      func: clock,
    },
  ],
}
const initLamp: Lamp = {
  color: { r: 0, g: 0, b: 0 },
}

const range = (n) => [...Array(n).keys()]
export const genLamps = () => {
  const lamps = range(NUMS).map(() => initLamp)

  for (const area of config.areas) {
    const alamps = area.func()

    for (const i of range(area.range)) {
      lamps[area.startAddress + i] = alamps[i]
    }
  }
}
