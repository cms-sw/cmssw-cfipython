import FWCore.ParameterSet.Config as cms

def SiPixelHLTSource(**kwargs):
  mod = cms.EDProducer('SiPixelHLTSource',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
