import FWCore.ParameterSet.Config as cms

def HFNoseVFEProducer(**kwargs):
  mod = cms.EDProducer('HFNoseVFEProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
