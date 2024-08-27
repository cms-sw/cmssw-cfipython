import FWCore.ParameterSet.Config as cms

def EtaPtMinGsfElectronSelector(**kwargs):
  mod = cms.EDFilter('EtaPtMinGsfElectronSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
