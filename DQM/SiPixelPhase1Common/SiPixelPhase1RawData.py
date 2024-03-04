import FWCore.ParameterSet.Config as cms

def SiPixelPhase1RawData(**kwargs):
  mod = cms.EDProducer('SiPixelPhase1RawData',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
