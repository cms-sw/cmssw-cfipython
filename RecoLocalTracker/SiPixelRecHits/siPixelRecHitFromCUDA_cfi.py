import FWCore.ParameterSet.Config as cms

siPixelRecHitFromCUDA = cms.EDProducer('SiPixelRecHitFromCUDA',
  pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingCUDA'),
  src = cms.InputTag('siPixelClustersPreSplitting'),
  mightGet = cms.optional.untracked.vstring
)
