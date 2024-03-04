import FWCore.ParameterSet.Config as cms

def GsfElectronSelector(**kwargs):
  mod = cms.EDFilter('GsfElectronSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
