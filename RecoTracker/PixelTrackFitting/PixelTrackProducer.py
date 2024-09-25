import FWCore.ParameterSet.Config as cms

def PixelTrackProducer(*args, **kwargs):
  mod = cms.EDProducer('PixelTrackProducer',
    passLabel = cms.string('pixelTracks'),
    SeedingHitSets = cms.InputTag('pixelTracksHitTriplets'),
    Fitter = cms.InputTag('pixelFitterByHelixProjections'),
    Filter = cms.InputTag('pixelTrackFilterByKinematics'),
    Cleaner = cms.string('pixelTrackCleanerBySharedHits'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
