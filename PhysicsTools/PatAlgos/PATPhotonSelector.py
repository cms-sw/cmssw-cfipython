import FWCore.ParameterSet.Config as cms

def PATPhotonSelector(*args, **kwargs):
  mod = cms.EDFilter('PATPhotonSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
