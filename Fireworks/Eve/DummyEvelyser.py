import FWCore.ParameterSet.Config as cms

def DummyEvelyser(**kwargs):
  mod = cms.EDAnalyzer('DummyEvelyser',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
