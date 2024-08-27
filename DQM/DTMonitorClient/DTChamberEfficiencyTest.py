import FWCore.ParameterSet.Config as cms

def DTChamberEfficiencyTest(**kwargs):
  mod = cms.EDProducer('DTChamberEfficiencyTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
