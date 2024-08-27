import FWCore.ParameterSet.Config as cms

def PtMinCandViewCloneSelector(**kwargs):
  mod = cms.EDFilter('PtMinCandViewCloneSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
