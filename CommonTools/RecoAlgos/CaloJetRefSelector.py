import FWCore.ParameterSet.Config as cms

def CaloJetRefSelector(*args, **kwargs):
  mod = cms.EDFilter('CaloJetRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
