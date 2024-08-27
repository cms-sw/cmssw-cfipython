import FWCore.ParameterSet.Config as cms

def DTChamberEfficiency(**kwargs):
  mod = cms.EDProducer('DTChamberEfficiency',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
