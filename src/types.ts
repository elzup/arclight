export type Lamp = {
  color: { r: number; g: number; b: number }
}
export type Sequence = Lamp[]

export type Area = {
  name: string
  startAddress: number
  range: number
  func: () => Sequence
}
