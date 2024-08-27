import FWCore.ParameterSet.Config as cms

def DummyCandSelector(**kwargs):
  mod = cms.EDFilter('DummyCandSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
