import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_PFRecHitHCALTopologyESProducer(*args, **kwargs):
  mod = cms.ESProducer('alpaka_rocm_async::PFRecHitHCALTopologyESProducer',
    usePFThresholdsFromDB = cms.bool(True),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
