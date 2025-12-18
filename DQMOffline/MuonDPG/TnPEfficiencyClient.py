import FWCore.ParameterSet.Config as cms

def TnPEfficiencyClient(*args, **kwargs):
  mod = cms.EDProducer('TnPEfficiencyClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
