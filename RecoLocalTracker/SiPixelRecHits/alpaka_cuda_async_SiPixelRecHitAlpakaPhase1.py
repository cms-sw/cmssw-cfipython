import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_SiPixelRecHitAlpakaPhase1(**kwargs):
  mod = cms.EDProducer('alpaka_cuda_async::SiPixelRecHitAlpakaPhase1',
    beamSpot = cms.InputTag('offlineBeamSpotDevice'),
    src = cms.InputTag('siPixelClustersPreSplittingAlpaka'),
    CPE = cms.string('PixelCPEFastParams'),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod