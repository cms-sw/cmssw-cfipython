import FWCore.ParameterSet.Config as cms

siPixelRecHitFromCUDAPhase2 = cms.EDProducer('SiPixelRecHitFromCUDAPhase2',
  pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingCUDA'),
  src = cms.InputTag('siPixelClustersPreSplitting'),
  mightGet = cms.optional.untracked.vstring
)
