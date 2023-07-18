import FWCore.ParameterSet.Config as cms

siPixelRecHitCUDAPhase2 = cms.EDProducer('SiPixelRecHitCUDAPhase2',
  beamSpot = cms.InputTag('offlineBeamSpotCUDA'),
  src = cms.InputTag('siPixelClustersPreSplittingCUDA'),
  CPE = cms.string('PixelCPEFastPhase2'),
  mightGet = cms.optional.untracked.vstring
)
