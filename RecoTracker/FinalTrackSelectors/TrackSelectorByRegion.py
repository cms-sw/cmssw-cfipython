import FWCore.ParameterSet.Config as cms

def TrackSelectorByRegion(**kwargs):
  mod = cms.EDProducer('TrackSelectorByRegion',
    tracks = cms.InputTag('hltPixelTracks'),
    regions = cms.InputTag(''),
    produceTrackCollection = cms.bool(True),
    produceMask = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
