import FWCore.ParameterSet.Config as cms

def TauSpinnerFilter(*args, **kwargs):
  mod = cms.EDFilter('TauSpinnerFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
