import FWCore.ParameterSet.Config as cms

def PixelColCleaner(*args, **kwargs):
  mod = cms.EDProducer('PixelColCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
