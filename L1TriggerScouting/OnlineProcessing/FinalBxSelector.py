import FWCore.ParameterSet.Config as cms

def FinalBxSelector(**kwargs):
  mod = cms.EDFilter('FinalBxSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
