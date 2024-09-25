import FWCore.ParameterSet.Config as cms

def PixelMatchGsfElectronShallowCloneProducer(*args, **kwargs):
  mod = cms.EDProducer('PixelMatchGsfElectronShallowCloneProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
