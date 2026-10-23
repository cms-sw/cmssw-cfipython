import FWCore.ParameterSet.Config as cms

def PixelColMerger(*args, **kwargs):
  mod = cms.EDProducer('PixelColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
