import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_BeamSpotDeviceProducer(**kwargs):
  mod = cms.EDProducer('alpaka_cuda_async::BeamSpotDeviceProducer',
    src = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
