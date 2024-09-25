import FWCore.ParameterSet.Config as cms

def MuonCalIsolationProducer(*args, **kwargs):
  mod = cms.EDProducer('MuonCalIsolationProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
