import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncSiPixelRecHitAlpakaPhase2 = cms.EDProducer('alpaka_cuda_async::SiPixelRecHitAlpakaPhase2',
  beamSpot = cms.InputTag('offlineBeamSpotDevice'),
  src = cms.InputTag('siPixelClustersPreSplittingAlpaka'),
  CPE = cms.string('PixelCPEFastParamsPhase2'),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
