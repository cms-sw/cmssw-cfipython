import FWCore.ParameterSet.Config as cms

def PFMETFilter(**kwargs):
  mod = cms.EDFilter('PFMETFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
