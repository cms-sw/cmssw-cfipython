import FWCore.ParameterSet.Config as cms

def LargestPtCandViewSelector(**kwargs):
  mod = cms.EDFilter('LargestPtCandViewSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
