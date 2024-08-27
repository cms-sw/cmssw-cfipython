import FWCore.ParameterSet.Config as cms

def DummyLHEAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('DummyLHEAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
