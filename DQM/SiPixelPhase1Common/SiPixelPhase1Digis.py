import FWCore.ParameterSet.Config as cms

def SiPixelPhase1Digis(**kwargs):
  mod = cms.EDProducer('SiPixelPhase1Digis',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
