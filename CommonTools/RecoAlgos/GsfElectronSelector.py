import FWCore.ParameterSet.Config as cms

def GsfElectronSelector(*args, **kwargs):
  mod = cms.EDFilter('GsfElectronSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
