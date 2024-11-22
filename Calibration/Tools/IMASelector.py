import FWCore.ParameterSet.Config as cms

def IMASelector(*args, **kwargs):
  mod = cms.EDFilter('IMASelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
