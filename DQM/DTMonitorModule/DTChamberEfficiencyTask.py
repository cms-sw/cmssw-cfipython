import FWCore.ParameterSet.Config as cms

def DTChamberEfficiencyTask(**kwargs):
  mod = cms.EDProducer('DTChamberEfficiencyTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
