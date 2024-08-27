import FWCore.ParameterSet.Config as cms

def Vx3DHLTAnalyzer(**kwargs):
  mod = cms.EDProducer('Vx3DHLTAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
