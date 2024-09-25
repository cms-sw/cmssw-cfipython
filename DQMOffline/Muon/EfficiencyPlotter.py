import FWCore.ParameterSet.Config as cms

def EfficiencyPlotter(*args, **kwargs):
  mod = cms.EDProducer('EfficiencyPlotter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
