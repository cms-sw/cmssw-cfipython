import FWCore.ParameterSet.Config as cms

def DTCompMapValidateDBRead(**kwargs):
  mod = cms.EDAnalyzer('DTCompMapValidateDBRead',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
