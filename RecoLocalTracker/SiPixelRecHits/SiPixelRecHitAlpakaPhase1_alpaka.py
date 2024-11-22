import FWCore.ParameterSet.Config as cms

def SiPixelRecHitAlpakaPhase1_alpaka(*args, **kwargs):
  mod = cms.EDProducer('SiPixelRecHitAlpakaPhase1@alpaka',
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
