import FWCore.ParameterSet.Config as cms

def TauValPFJetSelector(**kwargs):
  mod = cms.EDFilter('TauValPFJetSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod