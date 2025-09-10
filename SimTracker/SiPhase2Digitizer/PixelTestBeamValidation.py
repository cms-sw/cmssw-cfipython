import FWCore.ParameterSet.Config as cms

def PixelTestBeamValidation(*args, **kwargs):
  mod = cms.EDProducer('PixelTestBeamValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
