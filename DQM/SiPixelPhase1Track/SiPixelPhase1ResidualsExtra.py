import FWCore.ParameterSet.Config as cms

def SiPixelPhase1ResidualsExtra(**kwargs):
  mod = cms.EDProducer('SiPixelPhase1ResidualsExtra',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
