import FWCore.ParameterSet.Config as cms

def SimMuFilter(**kwargs):
  mod = cms.EDFilter('SimMuFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
