import FWCore.ParameterSet.Config as cms

def SiPixelPhase1HitsV(**kwargs):
  mod = cms.EDProducer('SiPixelPhase1HitsV',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
