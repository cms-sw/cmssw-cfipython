import FWCore.ParameterSet.Config as cms

def HcalMahiPulseOffsetsESProducer_alpaka(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
