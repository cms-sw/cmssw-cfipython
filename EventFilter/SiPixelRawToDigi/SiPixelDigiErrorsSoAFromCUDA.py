import FWCore.ParameterSet.Config as cms

def SiPixelDigiErrorsSoAFromCUDA(**kwargs):
  mod = cms.EDProducer('SiPixelDigiErrorsSoAFromCUDA',
    src = cms.InputTag('siPixelClustersCUDA'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
