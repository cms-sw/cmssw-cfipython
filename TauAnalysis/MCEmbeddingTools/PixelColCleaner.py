import FWCore.ParameterSet.Config as cms

def PixelColCleaner(**kwargs):
  mod = cms.EDProducer('PixelColCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
