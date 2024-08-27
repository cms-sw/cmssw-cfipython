import FWCore.ParameterSet.Config as cms

def LHEVpTFilter(**kwargs):
  mod = cms.EDFilter('LHEVpTFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
