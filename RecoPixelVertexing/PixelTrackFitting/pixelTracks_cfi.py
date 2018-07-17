import FWCore.ParameterSet.Config as cms

pixelTracks = cms.EDProducer('PixelTrackProducer',
  passLabel = cms.string('pixelTracks'),
  SeedingHitSets = cms.InputTag('pixelTracksHitTriplets'),
  Fitter = cms.InputTag('pixelFitterByHelixProjections'),
  Filter = cms.InputTag('pixelTrackFilterByKinematics'),
  Cleaner = cms.string('pixelTrackCleanerBySharedHits')
)
