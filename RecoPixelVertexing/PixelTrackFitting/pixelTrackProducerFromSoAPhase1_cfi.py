import FWCore.ParameterSet.Config as cms

pixelTrackProducerFromSoAPhase1 = cms.EDProducer('PixelTrackProducerFromSoAPhase1',
  beamSpot = cms.InputTag('offlineBeamSpot'),
  trackSrc = cms.InputTag('pixelTracksSoA'),
  pixelRecHitLegacySrc = cms.InputTag('siPixelRecHitsPreSplittingLegacy'),
  minNumberOfHits = cms.int32(0),
  minQuality = cms.string('loose'),
  mightGet = cms.optional.untracked.vstring
)