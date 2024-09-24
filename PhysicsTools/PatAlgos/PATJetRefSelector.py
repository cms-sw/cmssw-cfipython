import FWCore.ParameterSet.Config as cms

def PATJetRefSelector(*args, **kwargs):
  mod = cms.EDFilter('PATJetRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
