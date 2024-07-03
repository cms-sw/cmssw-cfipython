import FWCore.ParameterSet.Config as cms

siPixelRecHitAlpakaHIonPhase1 = cms.EDProducer('SiPixelRecHitAlpakaHIonPhase1@alpaka',
  beamSpot = cms.InputTag('offlineBeamSpotDevice'),
  src = cms.InputTag('siPixelClustersPreSplittingAlpaka'),
  CPE = cms.string('PixelCPEFastParamsHIonPhase1'),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
