import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncSiPixelRecHitAlpakaHIonPhase1 = cms.EDProducer('alpaka_rocm_async::SiPixelRecHitAlpakaHIonPhase1',
  beamSpot = cms.InputTag('offlineBeamSpotDevice'),
  src = cms.InputTag('siPixelClustersPreSplittingAlpaka'),
  CPE = cms.string('PixelCPEFastParamsHIonPhase1'),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
