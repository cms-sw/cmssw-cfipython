import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_PFRecHitECALParamsESProducer(*args, **kwargs):
  mod = cms.ESProducer('alpaka_rocm_async::PFRecHitECALParamsESProducer',
    cleaningThreshold = cms.double(2),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
