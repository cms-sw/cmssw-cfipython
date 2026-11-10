import FWCore.ParameterSet.Config as cms

def HLTPixelTrackSoATableProducer(*args, **kwargs):
  mod = cms.EDProducer('HLTPixelTrackSoATableProducer',
    skipNonExistingSrc = cms.bool(False),
    src = cms.InputTag('pixelTracksAlpaka'),
    name = cms.string('PixelTrackSoA'),
    doc = cms.string('Pixel tracks from TrackSoA'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
