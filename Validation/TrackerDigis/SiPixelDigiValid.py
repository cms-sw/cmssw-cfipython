import FWCore.ParameterSet.Config as cms

def SiPixelDigiValid(*args, **kwargs):
  mod = cms.EDProducer('SiPixelDigiValid',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
