import FWCore.ParameterSet.Config as cms

def MuScleFitFilter(*args, **kwargs):
  mod = cms.EDFilter('MuScleFitFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
