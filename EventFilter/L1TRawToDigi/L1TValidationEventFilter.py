import FWCore.ParameterSet.Config as cms

def L1TValidationEventFilter(*args, **kwargs):
  mod = cms.EDFilter('L1TValidationEventFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
