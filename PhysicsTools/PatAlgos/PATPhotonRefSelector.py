import FWCore.ParameterSet.Config as cms

def PATPhotonRefSelector(*args, **kwargs):
  mod = cms.EDFilter('PATPhotonRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
