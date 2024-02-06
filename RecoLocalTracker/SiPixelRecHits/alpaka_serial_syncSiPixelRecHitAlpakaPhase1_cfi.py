import FWCore.ParameterSet.Config as cms

alpaka_serial_syncSiPixelRecHitAlpakaPhase1 = cms.EDProducer('alpaka_serial_sync::SiPixelRecHitAlpakaPhase1',
  beamSpot = cms.InputTag('offlineBeamSpotDevice'),
  src = cms.InputTag('siPixelClustersPreSplittingAlpaka'),
  CPE = cms.string('PixelCPEFastParams'),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
