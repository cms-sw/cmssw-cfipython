import FWCore.ParameterSet.Config as cms

def LogErrorEventFilter(**kwargs):
  mod = cms.EDFilter('LogErrorEventFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
