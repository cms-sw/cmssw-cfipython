import FWCore.ParameterSet.Config as cms

def EtaPtMinPixelMatchGsfElectronSelector(**kwargs):
  mod = cms.EDFilter('EtaPtMinPixelMatchGsfElectronSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
