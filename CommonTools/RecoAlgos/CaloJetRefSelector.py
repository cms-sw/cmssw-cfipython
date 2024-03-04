import FWCore.ParameterSet.Config as cms

def CaloJetRefSelector(**kwargs):
  mod = cms.EDFilter('CaloJetRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
