import FWCore.ParameterSet.Config as cms

def PATElectronSlimmer(*args, **kwargs):
  mod = cms.EDProducer('PATElectronSlimmer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
