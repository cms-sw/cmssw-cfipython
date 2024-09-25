import FWCore.ParameterSet.Config as cms

def EtaPtMinPixelMatchGsfElectronFullCloneSelector(*args, **kwargs):
  mod = cms.EDFilter('EtaPtMinPixelMatchGsfElectronFullCloneSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
