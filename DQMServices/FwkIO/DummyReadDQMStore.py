import FWCore.ParameterSet.Config as cms

def DummyReadDQMStore(*args, **kwargs):
  mod = cms.EDAnalyzer('DummyReadDQMStore',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
