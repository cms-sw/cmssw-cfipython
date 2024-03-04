import FWCore.ParameterSet.Config as cms

def SiPixelPhase1Summary(**kwargs):
  mod = cms.EDProducer('SiPixelPhase1Summary',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
