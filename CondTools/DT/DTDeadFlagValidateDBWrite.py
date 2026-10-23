import FWCore.ParameterSet.Config as cms

def DTDeadFlagValidateDBWrite(*args, **kwargs):
  mod = cms.EDAnalyzer('DTDeadFlagValidateDBWrite',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
