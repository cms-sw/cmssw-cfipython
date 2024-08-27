import FWCore.ParameterSet.Config as cms

def SiPixelPhase1DigisV(**kwargs):
  mod = cms.EDProducer('SiPixelPhase1DigisV',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
