import FWCore.ParameterSet.Config as cms

def PATElectronSelector(**kwargs):
  mod = cms.EDFilter('PATElectronSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
