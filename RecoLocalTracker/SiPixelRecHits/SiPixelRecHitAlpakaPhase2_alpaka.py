import FWCore.ParameterSet.Config as cms

def SiPixelRecHitAlpakaPhase2_alpaka(*args, **kwargs):
  mod = cms.EDProducer('SiPixelRecHitAlpakaPhase2@alpaka',
    beamSpot = cms.InputTag('offlineBeamSpotDevice'),
    src = cms.InputTag('siPixelClustersPreSplittingAlpaka'),
    CPE = cms.string('PixelCPEFastParamsPhase2'),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
