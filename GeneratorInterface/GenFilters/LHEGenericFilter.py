import FWCore.ParameterSet.Config as cms

def LHEGenericFilter(**kwargs):
  mod = cms.EDFilter('LHEGenericFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
