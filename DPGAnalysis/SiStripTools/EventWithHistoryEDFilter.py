import FWCore.ParameterSet.Config as cms

def EventWithHistoryEDFilter(**kwargs):
  mod = cms.EDFilter('EventWithHistoryEDFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
