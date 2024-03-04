import FWCore.ParameterSet.Config as cms

def LargestEtCaloJetSelector(**kwargs):
  mod = cms.EDFilter('LargestEtCaloJetSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
