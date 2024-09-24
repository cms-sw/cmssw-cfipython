import FWCore.ParameterSet.Config as cms

def PickEvents(*args, **kwargs):
  mod = cms.EDFilter('PickEvents',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
