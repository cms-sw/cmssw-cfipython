import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncSiPixelRecHitAlpakaPhase1 = cms.EDProducer('alpaka_rocm_async::SiPixelRecHitAlpakaPhase1',
  beamSpot = cms.InputTag('offlineBeamSpotDevice'),
  src = cms.InputTag('siPixelClustersPreSplittingAlpaka'),
  CPE = cms.string('PixelCPEFastParams'),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
