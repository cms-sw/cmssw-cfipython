import FWCore.ParameterSet.Config as cms

siPixelRecHitSoAFromCUDAPhase2 = cms.EDProducer('SiPixelRecHitSoAFromCUDAPhase2',
  pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingCUDA'),
  mightGet = cms.optional.untracked.vstring
)
