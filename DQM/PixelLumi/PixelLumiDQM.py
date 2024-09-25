import FWCore.ParameterSet.Config as cms

def PixelLumiDQM(*args, **kwargs):
  mod = cms.EDProducer('PixelLumiDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
