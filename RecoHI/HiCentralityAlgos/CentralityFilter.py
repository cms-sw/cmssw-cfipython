import FWCore.ParameterSet.Config as cms

def CentralityFilter(**kwargs):
  mod = cms.EDFilter('CentralityFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
