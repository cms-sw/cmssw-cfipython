import FWCore.ParameterSet.Config as cms

def PixelTrackProducerFromSoAAlpakaPhase1(**kwargs):
  mod = cms.EDProducer('PixelTrackProducerFromSoAAlpakaPhase1',
    beamSpot = cms.InputTag('offlineBeamSpot'),
    trackSrc = cms.InputTag('pixelTracksAlpaka'),
    pixelRecHitLegacySrc = cms.InputTag('siPixelRecHitsPreSplittingLegacy'),
    minNumberOfHits = cms.int32(0),
    minQuality = cms.string('loose'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod