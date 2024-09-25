import FWCore.ParameterSet.Config as cms

def MuonIsolationDQM(*args, **kwargs):
  mod = cms.EDProducer('MuonIsolationDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
