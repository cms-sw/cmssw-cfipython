import FWCore.ParameterSet.Config as cms

def LHEPtFilter(**kwargs):
  mod = cms.EDFilter('LHEPtFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
