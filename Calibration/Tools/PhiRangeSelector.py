import FWCore.ParameterSet.Config as cms

def PhiRangeSelector(**kwargs):
  mod = cms.EDFilter('PhiRangeSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
