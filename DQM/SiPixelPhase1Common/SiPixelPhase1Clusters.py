import FWCore.ParameterSet.Config as cms

def SiPixelPhase1Clusters(**kwargs):
  mod = cms.EDProducer('SiPixelPhase1Clusters',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
