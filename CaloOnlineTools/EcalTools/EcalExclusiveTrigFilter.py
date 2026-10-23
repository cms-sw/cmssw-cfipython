import FWCore.ParameterSet.Config as cms

def EcalExclusiveTrigFilter(*args, **kwargs):
  mod = cms.EDFilter('EcalExclusiveTrigFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
