import FWCore.ParameterSet.Config as cms

def HLTBool(*args, **kwargs):
  mod = cms.EDFilter('HLTBool',
    result = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
