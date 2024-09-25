import FWCore.ParameterSet.Config as cms

def HcalMahiPulseOffsetsGPUESProducer(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
