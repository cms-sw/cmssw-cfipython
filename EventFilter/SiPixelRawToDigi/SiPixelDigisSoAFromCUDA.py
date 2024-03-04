import FWCore.ParameterSet.Config as cms

def SiPixelDigisSoAFromCUDA(**kwargs):
  mod = cms.EDProducer('SiPixelDigisSoAFromCUDA',
    src = cms.InputTag('siPixelClustersCUDA'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
