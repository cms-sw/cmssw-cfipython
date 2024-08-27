import FWCore.ParameterSet.Config as cms

def GsfElectronRefSelector(**kwargs):
  mod = cms.EDFilter('GsfElectronRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
