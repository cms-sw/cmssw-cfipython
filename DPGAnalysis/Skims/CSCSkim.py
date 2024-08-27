import FWCore.ParameterSet.Config as cms

def CSCSkim(**kwargs):
  mod = cms.EDFilter('CSCSkim',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
