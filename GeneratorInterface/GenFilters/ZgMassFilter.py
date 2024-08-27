import FWCore.ParameterSet.Config as cms

def ZgMassFilter(**kwargs):
  mod = cms.EDFilter('ZgMassFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
