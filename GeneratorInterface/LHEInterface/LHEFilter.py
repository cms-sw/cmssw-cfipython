import FWCore.ParameterSet.Config as cms

def LHEFilter(**kwargs):
  mod = cms.EDFilter('LHEFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
