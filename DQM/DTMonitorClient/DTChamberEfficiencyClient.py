import FWCore.ParameterSet.Config as cms

def DTChamberEfficiencyClient(**kwargs):
  mod = cms.EDProducer('DTChamberEfficiencyClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
