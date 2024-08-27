import FWCore.ParameterSet.Config as cms

def DTT0ValidateDBRead(**kwargs):
  mod = cms.EDAnalyzer('DTT0ValidateDBRead',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
