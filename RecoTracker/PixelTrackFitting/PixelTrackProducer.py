import FWCore.ParameterSet.Config as cms

def PixelTrackProducer(**kwargs):
  mod = cms.EDProducer('PixelTrackProducer',
    passLabel = cms.string('pixelTracks'),
    SeedingHitSets = cms.InputTag('pixelTracksHitTriplets'),
    Fitter = cms.InputTag('pixelFitterByHelixProjections'),
    Filter = cms.InputTag('pixelTrackFilterByKinematics'),
    Cleaner = cms.string('pixelTrackCleanerBySharedHits'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
