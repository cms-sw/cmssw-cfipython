import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_PFRecHitHCALParamsESProducer(*args, **kwargs):
  mod = cms.ESProducer('alpaka_cuda_async::PFRecHitHCALParamsESProducer',
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
