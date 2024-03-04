import FWCore.ParameterSet.Config as cms

def HighMultiplicityGenFilter(**kwargs):
  mod = cms.EDFilter('HighMultiplicityGenFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
