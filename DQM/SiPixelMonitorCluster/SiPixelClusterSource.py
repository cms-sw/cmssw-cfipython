import FWCore.ParameterSet.Config as cms

def SiPixelClusterSource(**kwargs):
  mod = cms.EDProducer('SiPixelClusterSource',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
