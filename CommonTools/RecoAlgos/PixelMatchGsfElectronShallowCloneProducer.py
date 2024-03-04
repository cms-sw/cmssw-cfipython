import FWCore.ParameterSet.Config as cms

def PixelMatchGsfElectronShallowCloneProducer(**kwargs):
  mod = cms.EDProducer('PixelMatchGsfElectronShallowCloneProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
