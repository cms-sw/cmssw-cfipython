import FWCore.ParameterSet.Config as cms

def L3MuonIsolationProducer(**kwargs):
  mod = cms.EDProducer('L3MuonIsolationProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
