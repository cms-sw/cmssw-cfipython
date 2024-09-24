import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_PFRecHitHCALParamsESProducer(**kwargs):
  mod = cms.ESProducer('alpaka_rocm_async::PFRecHitHCALParamsESProducer',
    energyThresholdsHB = cms.vdouble(
      0.1,
      0.2,
      0.3,
      0.3
    ),
    energyThresholdsHE = cms.vdouble(
      0.1,
      0.2,
      0.2,
      0.2,
      0.2,
      0.2,
      0.2
    ),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod