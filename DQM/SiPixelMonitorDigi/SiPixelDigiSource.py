import FWCore.ParameterSet.Config as cms

def SiPixelDigiSource(**kwargs):
  mod = cms.EDProducer('SiPixelDigiSource',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
