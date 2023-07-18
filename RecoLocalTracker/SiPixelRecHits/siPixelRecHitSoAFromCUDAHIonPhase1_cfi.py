import FWCore.ParameterSet.Config as cms

siPixelRecHitSoAFromCUDAHIonPhase1 = cms.EDProducer('SiPixelRecHitSoAFromCUDAHIonPhase1',
  pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingCUDA'),
  mightGet = cms.optional.untracked.vstring
)
