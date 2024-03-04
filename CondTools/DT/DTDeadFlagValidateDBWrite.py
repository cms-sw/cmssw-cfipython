import FWCore.ParameterSet.Config as cms

def DTDeadFlagValidateDBWrite(**kwargs):
  mod = cms.EDAnalyzer('DTDeadFlagValidateDBWrite',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
