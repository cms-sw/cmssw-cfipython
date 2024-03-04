import FWCore.ParameterSet.Config as cms

def SiPixelStatusHarvester(**kwargs):
  mod = cms.EDProducer('SiPixelStatusHarvester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
