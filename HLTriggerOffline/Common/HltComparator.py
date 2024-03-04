import FWCore.ParameterSet.Config as cms

def HltComparator(**kwargs):
  mod = cms.EDFilter('HltComparator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
