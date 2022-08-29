import FWCore.ParameterSet.Config as cms

siPixelRecHitCUDA = cms.EDProducer('SiPixelRecHitCUDA',
  beamSpot = cms.InputTag('offlineBeamSpotCUDA'),
  src = cms.InputTag('siPixelClustersPreSplittingCUDA'),
  CPE = cms.string('PixelCPEFast'),
  mightGet = cms.optional.untracked.vstring
)
