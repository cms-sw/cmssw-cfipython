import FWCore.ParameterSet.Config as cms

def DummyReadDQMStore(**kwargs):
  mod = cms.EDAnalyzer('DummyReadDQMStore',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
