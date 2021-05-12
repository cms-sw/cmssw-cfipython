import FWCore.ParameterSet.Config as cms

pixelTrackProducerFromSoA = cms.EDProducer('PixelTrackProducerFromSoA',
  beamSpot = cms.InputTag('offlineBeamSpot'),
  trackSrc = cms.InputTag('pixelTracksSoA'),
  pixelRecHitLegacySrc = cms.InputTag('siPixelRecHitsPreSplittingLegacy'),
  minNumberOfHits = cms.int32(0),
  mightGet = cms.optional.untracked.vstring
)
