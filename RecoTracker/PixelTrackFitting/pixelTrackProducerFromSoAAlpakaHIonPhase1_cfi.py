import FWCore.ParameterSet.Config as cms

pixelTrackProducerFromSoAAlpakaHIonPhase1 = cms.EDProducer('PixelTrackProducerFromSoAAlpakaHIonPhase1',
  beamSpot = cms.InputTag('offlineBeamSpot'),
  trackSrc = cms.InputTag('pixelTracksAlpaka'),
  pixelRecHitLegacySrc = cms.InputTag('siPixelRecHitsPreSplittingLegacy'),
  minNumberOfHits = cms.int32(0),
  minQuality = cms.string('loose'),
  mightGet = cms.optional.untracked.vstring
)
