import FWCore.ParameterSet.Config as cms

def EfficiencyAnalyzer(**kwargs):
  mod = cms.EDProducer('EfficiencyAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
