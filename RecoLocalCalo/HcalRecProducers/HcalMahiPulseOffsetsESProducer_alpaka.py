import FWCore.ParameterSet.Config as cms

def HcalMahiPulseOffsetsESProducer_alpaka(**kwargs):
  mod = cms.ESProducer('HcalMahiPulseOffsetsESProducer@alpaka',
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
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
