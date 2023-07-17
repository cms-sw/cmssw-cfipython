import FWCore.ParameterSet.Config as cms

siPixelRecHitCUDAHIonPhase1 = cms.EDProducer('SiPixelRecHitCUDAHIonPhase1',
  beamSpot = cms.InputTag('offlineBeamSpotCUDA'),
  src = cms.InputTag('siPixelClustersPreSplittingCUDA'),
  CPE = cms.string('PixelCPEFastHIonPhase1'),
  mightGet = cms.optional.untracked.vstring
)
