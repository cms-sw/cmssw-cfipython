import FWCore.ParameterSet.Config as cms

def EfficiencyPlotter(**kwargs):
  mod = cms.EDProducer('EfficiencyPlotter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
