import FWCore.ParameterSet.Config as cms

def EtaPtMinGsfElectronFullCloneSelector(*args, **kwargs):
  mod = cms.EDFilter('EtaPtMinGsfElectronFullCloneSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
