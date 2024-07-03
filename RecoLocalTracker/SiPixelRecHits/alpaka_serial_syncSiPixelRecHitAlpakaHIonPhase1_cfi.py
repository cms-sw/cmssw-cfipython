import FWCore.ParameterSet.Config as cms

alpaka_serial_syncSiPixelRecHitAlpakaHIonPhase1 = cms.EDProducer('alpaka_serial_sync::SiPixelRecHitAlpakaHIonPhase1',
  beamSpot = cms.InputTag('offlineBeamSpotDevice'),
  src = cms.InputTag('siPixelClustersPreSplittingAlpaka'),
  CPE = cms.string('PixelCPEFastParamsHIonPhase1'),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
