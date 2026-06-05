import FWCore.ParameterSet.Config as cms

def L3MuonIsolationProducer(*args, **kwargs):
  mod = cms.EDProducer('L3MuonIsolationProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
