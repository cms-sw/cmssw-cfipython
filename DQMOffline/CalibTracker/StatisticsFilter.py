import FWCore.ParameterSet.Config as cms

def StatisticsFilter(**kwargs):
  mod = cms.EDFilter('StatisticsFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
