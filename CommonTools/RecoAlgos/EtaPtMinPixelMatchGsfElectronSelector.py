import FWCore.ParameterSet.Config as cms

def EtaPtMinPixelMatchGsfElectronSelector(*args, **kwargs):
  mod = cms.EDFilter('EtaPtMinPixelMatchGsfElectronSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
