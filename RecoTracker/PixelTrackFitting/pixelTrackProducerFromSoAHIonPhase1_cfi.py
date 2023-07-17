import FWCore.ParameterSet.Config as cms

pixelTrackProducerFromSoAHIonPhase1 = cms.EDProducer('PixelTrackProducerFromSoAHIonPhase1',
  beamSpot = cms.InputTag('offlineBeamSpot'),
  trackSrc = cms.InputTag('pixelTracksSoA'),
  pixelRecHitLegacySrc = cms.InputTag('siPixelRecHitsPreSplittingLegacy'),
  minNumberOfHits = cms.int32(0),
  minQuality = cms.string('loose'),
  mightGet = cms.optional.untracked.vstring
)
