import FWCore.ParameterSet.Config as cms

siPixelRecHitAlpakaPhase1 = cms.EDProducer('SiPixelRecHitAlpakaPhase1@alpaka',
  beamSpot = cms.InputTag('offlineBeamSpotDevice'),
  src = cms.InputTag('siPixelClustersPreSplittingAlpaka'),
  CPE = cms.string('PixelCPEFastParams'),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
