import FWCore.ParameterSet.Config as cms

def PixelTracksProducer(*args, **kwargs):
  mod = cms.EDProducer('PixelTracksProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
