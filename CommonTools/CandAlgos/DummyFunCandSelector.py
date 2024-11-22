import FWCore.ParameterSet.Config as cms

def DummyFunCandSelector(*args, **kwargs):
  mod = cms.EDFilter('DummyFunCandSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
