import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_SiPixelRecHitAlpakaHIonPhase1(*args, **kwargs):
  mod = cms.EDProducer('alpaka_cuda_async::SiPixelRecHitAlpakaHIonPhase1',
    beamSpot = cms.InputTag('offlineBeamSpotDevice'),
    src = cms.InputTag('siPixelClustersPreSplittingAlpaka'),
    CPE = cms.string('PixelCPEFastParamsHIonPhase1'),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
