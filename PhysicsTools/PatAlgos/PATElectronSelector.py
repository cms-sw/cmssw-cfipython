import FWCore.ParameterSet.Config as cms

def PATElectronSelector(*args, **kwargs):
  mod = cms.EDFilter('PATElectronSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
