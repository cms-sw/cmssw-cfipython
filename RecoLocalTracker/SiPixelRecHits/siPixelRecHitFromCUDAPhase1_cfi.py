import FWCore.ParameterSet.Config as cms

siPixelRecHitFromCUDAPhase1 = cms.EDProducer('SiPixelRecHitFromCUDAPhase1',
  pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingCUDA'),
  src = cms.InputTag('siPixelClustersPreSplitting'),
  mightGet = cms.optional.untracked.vstring
)
