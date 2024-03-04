import FWCore.ParameterSet.Config as cms

def PixelTestBeamValidation(**kwargs):
  mod = cms.EDProducer('PixelTestBeamValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
