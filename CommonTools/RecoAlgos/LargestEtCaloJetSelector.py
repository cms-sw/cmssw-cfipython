import FWCore.ParameterSet.Config as cms

def LargestEtCaloJetSelector(*args, **kwargs):
  mod = cms.EDFilter('LargestEtCaloJetSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
