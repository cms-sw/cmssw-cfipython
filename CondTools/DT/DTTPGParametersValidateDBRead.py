import FWCore.ParameterSet.Config as cms

def DTTPGParametersValidateDBRead(**kwargs):
  mod = cms.EDAnalyzer('DTTPGParametersValidateDBRead',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
