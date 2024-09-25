import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_PFRecHitECALTopologyESProducer(*args, **kwargs):
  mod = cms.ESProducer('alpaka_cuda_async::PFRecHitECALTopologyESProducer',
    usePFThresholdsFromDB = cms.bool(False),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
