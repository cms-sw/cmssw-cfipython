import FWCore.ParameterSet.Config as cms

def EtaPtMinGsfElectronSelector(*args, **kwargs):
  mod = cms.EDFilter('EtaPtMinGsfElectronSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
