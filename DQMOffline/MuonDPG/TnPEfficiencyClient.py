import FWCore.ParameterSet.Config as cms

def TnPEfficiencyClient(**kwargs):
  mod = cms.EDProducer('TnPEfficiencyClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
