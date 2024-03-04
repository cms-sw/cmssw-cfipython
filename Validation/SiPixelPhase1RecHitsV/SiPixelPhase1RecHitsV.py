import FWCore.ParameterSet.Config as cms

def SiPixelPhase1RecHitsV(**kwargs):
  mod = cms.EDProducer('SiPixelPhase1RecHitsV',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
