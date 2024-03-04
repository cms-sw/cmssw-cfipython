import FWCore.ParameterSet.Config as cms

def DTMtimeValidateDBRead(**kwargs):
  mod = cms.EDAnalyzer('DTMtimeValidateDBRead',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
