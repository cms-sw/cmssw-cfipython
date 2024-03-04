import FWCore.ParameterSet.Config as cms

def SiPixelDcsInfo(**kwargs):
  mod = cms.EDProducer('SiPixelDcsInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
