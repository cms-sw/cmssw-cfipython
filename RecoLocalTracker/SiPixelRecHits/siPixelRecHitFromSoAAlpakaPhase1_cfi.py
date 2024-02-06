import FWCore.ParameterSet.Config as cms

siPixelRecHitFromSoAAlpakaPhase1 = cms.EDProducer('SiPixelRecHitFromSoAAlpakaPhase1',
  pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingAlpaka'),
  src = cms.InputTag('siPixelClustersPreSplitting'),
  mightGet = cms.optional.untracked.vstring
)
