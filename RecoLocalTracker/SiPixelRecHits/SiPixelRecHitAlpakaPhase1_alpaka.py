import FWCore.ParameterSet.Config as cms

def SiPixelRecHitAlpakaPhase1_alpaka(**kwargs):
  mod = cms.EDProducer('SiPixelRecHitAlpakaPhase1@alpaka',
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
