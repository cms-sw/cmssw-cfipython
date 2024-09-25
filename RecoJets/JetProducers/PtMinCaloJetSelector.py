import FWCore.ParameterSet.Config as cms

def PtMinCaloJetSelector(*args, **kwargs):
  mod = cms.EDFilter('PtMinCaloJetSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
