import FWCore.ParameterSet.Config as cms

def SiPixelFedFillerWordEventNumber(**kwargs):
  mod = cms.EDProducer('SiPixelFedFillerWordEventNumber',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
