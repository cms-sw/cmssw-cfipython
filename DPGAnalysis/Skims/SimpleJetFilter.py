import FWCore.ParameterSet.Config as cms

def SimpleJetFilter(**kwargs):
  mod = cms.EDFilter('SimpleJetFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
