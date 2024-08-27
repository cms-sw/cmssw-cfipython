import FWCore.ParameterSet.Config as cms

def PATJetRefSelector(**kwargs):
  mod = cms.EDFilter('PATJetRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
