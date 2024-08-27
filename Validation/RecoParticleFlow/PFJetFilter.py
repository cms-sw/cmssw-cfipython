import FWCore.ParameterSet.Config as cms

def PFJetFilter(**kwargs):
  mod = cms.EDFilter('PFJetFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
