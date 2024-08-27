import FWCore.ParameterSet.Config as cms

def JetHTJetPlusHOFilter(**kwargs):
  mod = cms.EDFilter('JetHTJetPlusHOFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
