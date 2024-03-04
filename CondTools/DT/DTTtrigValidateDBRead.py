import FWCore.ParameterSet.Config as cms

def DTTtrigValidateDBRead(**kwargs):
  mod = cms.EDAnalyzer('DTTtrigValidateDBRead',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
