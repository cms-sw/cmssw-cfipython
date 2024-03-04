import FWCore.ParameterSet.Config as cms

def TauValElectronSelector(**kwargs):
  mod = cms.EDFilter('TauValElectronSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
