import FWCore.ParameterSet.Config as cms

def SiPixelPhase1EfficiencyExtras(**kwargs):
  mod = cms.EDProducer('SiPixelPhase1EfficiencyExtras',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod