import FWCore.ParameterSet.Config as cms

def TrackSelectorByRegion(*args, **kwargs):
  mod = cms.EDProducer('TrackSelectorByRegion',
    tracks = cms.InputTag('hltPixelTracks'),
    regions = cms.InputTag(''),
    produceTrackCollection = cms.bool(True),
    produceMask = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
