import FWCore.ParameterSet.Config as cms

def DTStatusFlagValidateDBWrite(*args, **kwargs):
  mod = cms.EDAnalyzer('DTStatusFlagValidateDBWrite',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
