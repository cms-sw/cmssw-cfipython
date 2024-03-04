import FWCore.ParameterSet.Config as cms

def DummyFunCandSelector(**kwargs):
  mod = cms.EDFilter('DummyFunCandSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
