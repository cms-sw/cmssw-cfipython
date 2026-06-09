import FWCore.ParameterSet.Config as cms

def HLTPixelTrackFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTPixelTrackFilter',
    saveTags = cms.bool(True),
    pixelTracks = cms.InputTag('hltPixelTracks'),
    minPixelTracks = cms.uint32(0),
    maxPixelTracks = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
