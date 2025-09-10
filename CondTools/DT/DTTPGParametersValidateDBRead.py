import FWCore.ParameterSet.Config as cms

def DTTPGParametersValidateDBRead(*args, **kwargs):
  mod = cms.EDAnalyzer('DTTPGParametersValidateDBRead',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
