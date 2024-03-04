import FWCore.ParameterSet.Config as cms

def HLTPixelTrackFilter(**kwargs):
  mod = cms.EDFilter('HLTPixelTrackFilter',
    pixelTracks = cms.InputTag('hltPixelTracks'),
    minPixelTracks = cms.uint32(0),
    maxPixelTracks = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
