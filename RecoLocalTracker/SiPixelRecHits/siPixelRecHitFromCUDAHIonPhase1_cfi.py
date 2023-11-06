import FWCore.ParameterSet.Config as cms

siPixelRecHitFromCUDAHIonPhase1 = cms.EDProducer('SiPixelRecHitFromCUDAHIonPhase1',
  pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingCUDA'),
  src = cms.InputTag('siPixelClustersPreSplitting'),
  mightGet = cms.optional.untracked.vstring
)
