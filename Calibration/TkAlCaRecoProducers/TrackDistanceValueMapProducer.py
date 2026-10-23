import FWCore.ParameterSet.Config as cms

def TrackDistanceValueMapProducer(*args, **kwargs):
  mod = cms.EDProducer('TrackDistanceValueMapProducer',
    muonTracks = cms.InputTag('ALCARECOSiPixelCalSingleMuonTight'),
    allTracks = cms.InputTag('generalTracks'),
    saveUpToNthClosest = cms.uint32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
