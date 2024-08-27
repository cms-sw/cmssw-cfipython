import FWCore.ParameterSet.Config as cms

def SiPixelPhase1RecHits(**kwargs):
  mod = cms.EDProducer('SiPixelPhase1RecHits',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
