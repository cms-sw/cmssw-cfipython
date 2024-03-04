import FWCore.ParameterSet.Config as cms

def GEMTnPEfficiencyTask(**kwargs):
  mod = cms.EDProducer('GEMTnPEfficiencyTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
