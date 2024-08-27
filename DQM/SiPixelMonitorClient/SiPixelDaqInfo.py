import FWCore.ParameterSet.Config as cms

def SiPixelDaqInfo(**kwargs):
  mod = cms.EDProducer('SiPixelDaqInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
