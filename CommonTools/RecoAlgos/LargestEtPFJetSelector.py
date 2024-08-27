import FWCore.ParameterSet.Config as cms

def LargestEtPFJetSelector(**kwargs):
  mod = cms.EDFilter('LargestEtPFJetSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
