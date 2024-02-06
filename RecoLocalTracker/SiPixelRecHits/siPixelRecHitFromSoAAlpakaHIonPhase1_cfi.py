import FWCore.ParameterSet.Config as cms

siPixelRecHitFromSoAAlpakaHIonPhase1 = cms.EDProducer('SiPixelRecHitFromSoAAlpakaHIonPhase1',
  pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingAlpaka'),
  src = cms.InputTag('siPixelClustersPreSplitting'),
  mightGet = cms.optional.untracked.vstring
)
