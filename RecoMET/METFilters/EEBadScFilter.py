import FWCore.ParameterSet.Config as cms

def EEBadScFilter(*args, **kwargs):
  mod = cms.EDFilter('EEBadScFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
