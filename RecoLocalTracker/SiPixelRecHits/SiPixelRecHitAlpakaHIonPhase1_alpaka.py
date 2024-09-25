import FWCore.ParameterSet.Config as cms

def SiPixelRecHitAlpakaHIonPhase1_alpaka(*args, **kwargs):
  mod = cms.EDProducer('SiPixelRecHitAlpakaHIonPhase1@alpaka',
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
