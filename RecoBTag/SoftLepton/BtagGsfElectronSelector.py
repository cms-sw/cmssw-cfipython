import FWCore.ParameterSet.Config as cms

def BtagGsfElectronSelector(*args, **kwargs):
  mod = cms.EDProducer('BtagGsfElectronSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
