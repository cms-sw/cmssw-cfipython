import FWCore.ParameterSet.Config as cms

def SiPixelDigiValid(**kwargs):
  mod = cms.EDProducer('SiPixelDigiValid',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
