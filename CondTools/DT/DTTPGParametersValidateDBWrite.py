import FWCore.ParameterSet.Config as cms

def DTTPGParametersValidateDBWrite(**kwargs):
  mod = cms.EDAnalyzer('DTTPGParametersValidateDBWrite',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
