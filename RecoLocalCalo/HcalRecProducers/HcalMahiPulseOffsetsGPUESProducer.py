import FWCore.ParameterSet.Config as cms

def HcalMahiPulseOffsetsGPUESProducer(**kwargs):
  mod = cms.ESSource('HcalMahiPulseOffsetsGPUESProducer',
    pulseOffsets = cms.vint32(
      -3,
      -2,
      -1,
      0,
      1,
      2,
      3,
      4
    ),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
