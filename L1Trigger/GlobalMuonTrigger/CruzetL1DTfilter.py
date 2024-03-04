import FWCore.ParameterSet.Config as cms

def CruzetL1DTfilter(**kwargs):
  mod = cms.EDFilter('CruzetL1DTfilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
