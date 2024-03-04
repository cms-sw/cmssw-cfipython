import FWCore.ParameterSet.Config as cms

def SiPixelPhase1DeadFEDChannels(**kwargs):
  mod = cms.EDProducer('SiPixelPhase1DeadFEDChannels',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
