import FWCore.ParameterSet.Config as cms

def EtMinCaloJetRefSelector(*args, **kwargs):
  mod = cms.EDFilter('EtMinCaloJetRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
