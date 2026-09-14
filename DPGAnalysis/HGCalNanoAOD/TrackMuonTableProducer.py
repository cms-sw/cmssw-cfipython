import FWCore.ParameterSet.Config as cms

def TrackMuonTableProducer(*args, **kwargs):
  mod = cms.EDProducer('TrackMuonTableProducer',
    tracks = cms.InputTag('generalTracks'),
    muons = cms.InputTag('muons1stStep'),
    name = cms.string('TrackMuon'),
    doc = cms.string('Muons matched to GeneralTrack, one row per muon'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
