import FWCore.ParameterSet.Config as cms

def PixelTrackProducerFromSoAAlpakaPhase2(*args, **kwargs):
  mod = cms.EDProducer('PixelTrackProducerFromSoAAlpakaPhase2',
    beamSpot = cms.InputTag('offlineBeamSpot'),
    trackSrc = cms.InputTag('pixelTracksAlpaka'),
    pixelRecHitLegacySrc = cms.InputTag('siPixelRecHitsPreSplittingLegacy'),
    minNumberOfHits = cms.int32(0),
    minQuality = cms.string('loose'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
