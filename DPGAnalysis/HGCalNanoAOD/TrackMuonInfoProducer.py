import FWCore.ParameterSet.Config as cms

def TrackMuonInfoProducer(*args, **kwargs):
  mod = cms.EDProducer('TrackMuonInfoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
