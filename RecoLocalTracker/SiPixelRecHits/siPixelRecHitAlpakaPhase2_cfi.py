import FWCore.ParameterSet.Config as cms

siPixelRecHitAlpakaPhase2 = cms.EDProducer('SiPixelRecHitAlpakaPhase2@alpaka',
  beamSpot = cms.InputTag('offlineBeamSpotDevice'),
  src = cms.InputTag('siPixelClustersPreSplittingAlpaka'),
  CPE = cms.string('PixelCPEFastParamsPhase2'),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)