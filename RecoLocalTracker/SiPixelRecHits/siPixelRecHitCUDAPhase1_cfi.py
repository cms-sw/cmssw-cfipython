import FWCore.ParameterSet.Config as cms

siPixelRecHitCUDAPhase1 = cms.EDProducer('SiPixelRecHitCUDAPhase1',
  beamSpot = cms.InputTag('offlineBeamSpotCUDA'),
  src = cms.InputTag('siPixelClustersPreSplittingCUDA'),
  CPE = cms.string('PixelCPEFast'),
  mightGet = cms.optional.untracked.vstring
)
