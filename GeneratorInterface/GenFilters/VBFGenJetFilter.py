import FWCore.ParameterSet.Config as cms

def VBFGenJetFilter(**kwargs):
  mod = cms.EDFilter('VBFGenJetFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
