import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_HcalMahiPulseOffsetsESProducer(**kwargs):
  mod = cms.ESProducer('alpaka_rocm_async::HcalMahiPulseOffsetsESProducer',
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
