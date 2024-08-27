import FWCore.ParameterSet.Config as cms

def SiPixelPhase1DigisHarvesterV(**kwargs):
  mod = cms.EDProducer('SiPixelPhase1DigisHarvesterV',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
