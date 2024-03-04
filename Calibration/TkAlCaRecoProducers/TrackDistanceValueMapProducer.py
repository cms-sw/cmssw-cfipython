import FWCore.ParameterSet.Config as cms

def TrackDistanceValueMapProducer(**kwargs):
  mod = cms.EDProducer('TrackDistanceValueMapProducer',
    muonTracks = cms.InputTag('ALCARECOSiPixelCalSingleMuonTight'),
    allTracks = cms.InputTag('generalTracks'),
    saveUpToNthClosest = cms.uint32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
