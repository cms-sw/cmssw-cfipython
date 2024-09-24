import FWCore.ParameterSet.Config as cms

def PATElectronRefSelector(*args, **kwargs):
  mod = cms.EDFilter('PATElectronRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
