import FWCore.ParameterSet.Config as cms

alpaka_serial_syncSiPixelRecHitAlpakaPhase2 = cms.EDProducer('alpaka_serial_sync::SiPixelRecHitAlpakaPhase2',
  beamSpot = cms.InputTag('offlineBeamSpotDevice'),
  src = cms.InputTag('siPixelClustersPreSplittingAlpaka'),
  CPE = cms.string('PixelCPEFastParamsPhase2'),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
