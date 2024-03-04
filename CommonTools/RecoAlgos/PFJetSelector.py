import FWCore.ParameterSet.Config as cms

def PFJetSelector(**kwargs):
  mod = cms.EDFilter('PFJetSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
