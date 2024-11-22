import FWCore.ParameterSet.Config as cms

def LargestEtPFJetSelector(*args, **kwargs):
  mod = cms.EDFilter('LargestEtPFJetSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
