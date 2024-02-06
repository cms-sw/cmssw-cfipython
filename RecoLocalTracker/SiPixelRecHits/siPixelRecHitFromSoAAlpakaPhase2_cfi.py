import FWCore.ParameterSet.Config as cms

siPixelRecHitFromSoAAlpakaPhase2 = cms.EDProducer('SiPixelRecHitFromSoAAlpakaPhase2',
  pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingAlpaka'),
  src = cms.InputTag('siPixelClustersPreSplitting'),
  mightGet = cms.optional.untracked.vstring
)
