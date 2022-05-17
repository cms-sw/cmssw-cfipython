import FWCore.ParameterSet.Config as cms

siPixelRecHitSoAFromCUDA = cms.EDProducer('SiPixelRecHitSoAFromCUDA',
  pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingCUDA'),
  mightGet = cms.optional.untracked.vstring
)
