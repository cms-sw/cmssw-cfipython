import FWCore.ParameterSet.Config as cms

def CandViewSelector(**kwargs):
  mod = cms.EDFilter('CandViewSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
