import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_SiPixelRecHitAlpakaPhase1(*args, **kwargs):
  mod = cms.EDProducer('alpaka_rocm_async::SiPixelRecHitAlpakaPhase1',
    beamSpot = cms.InputTag('offlineBeamSpotDevice'),
    src = cms.InputTag('siPixelClustersPreSplittingAlpaka'),
    CPE = cms.string('PixelCPEFastParams'),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
