import FWCore.ParameterSet.Config as cms

def PATMETRefSelector(*args, **kwargs):
  mod = cms.EDFilter('PATMETRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
