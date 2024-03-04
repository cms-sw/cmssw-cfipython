import FWCore.ParameterSet.Config as cms

def PtMinPFJetSelector(**kwargs):
  mod = cms.EDFilter('PtMinPFJetSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
