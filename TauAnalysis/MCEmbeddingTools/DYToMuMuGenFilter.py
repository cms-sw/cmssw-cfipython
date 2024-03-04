import FWCore.ParameterSet.Config as cms

def DYToMuMuGenFilter(**kwargs):
  mod = cms.EDFilter('DYToMuMuGenFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
