import FWCore.ParameterSet.Config as cms

def DTTPGParametersValidateDBWrite(*args, **kwargs):
  mod = cms.EDAnalyzer('DTTPGParametersValidateDBWrite',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
