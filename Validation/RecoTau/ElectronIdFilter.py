import FWCore.ParameterSet.Config as cms

def ElectronIdFilter(*args, **kwargs):
  mod = cms.EDFilter('ElectronIdFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
