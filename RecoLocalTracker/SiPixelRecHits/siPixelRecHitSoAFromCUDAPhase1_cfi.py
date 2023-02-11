import FWCore.ParameterSet.Config as cms

siPixelRecHitSoAFromCUDAPhase1 = cms.EDProducer('SiPixelRecHitSoAFromCUDAPhase1',
  pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingCUDA'),
  mightGet = cms.optional.untracked.vstring
)
