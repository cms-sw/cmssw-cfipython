import FWCore.ParameterSet.Config as cms

def ElectronIdFilter(**kwargs):
  mod = cms.EDFilter('ElectronIdFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
