import FWCore.ParameterSet.Config as cms

def SiPixelEDAClient(**kwargs):
  mod = cms.EDProducer('SiPixelEDAClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
