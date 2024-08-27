import FWCore.ParameterSet.Config as cms

def DTEfficiencyTest(**kwargs):
  mod = cms.EDProducer('DTEfficiencyTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
