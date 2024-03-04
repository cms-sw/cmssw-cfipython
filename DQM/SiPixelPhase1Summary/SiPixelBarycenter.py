import FWCore.ParameterSet.Config as cms

def SiPixelBarycenter(**kwargs):
  mod = cms.EDProducer('SiPixelBarycenter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
