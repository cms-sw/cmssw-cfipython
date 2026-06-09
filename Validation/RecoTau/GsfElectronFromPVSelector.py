import FWCore.ParameterSet.Config as cms

def GsfElectronFromPVSelector(*args, **kwargs):
  mod = cms.EDProducer('GsfElectronFromPVSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
