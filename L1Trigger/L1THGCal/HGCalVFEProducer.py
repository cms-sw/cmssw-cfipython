import FWCore.ParameterSet.Config as cms

def HGCalVFEProducer(**kwargs):
  mod = cms.EDProducer('HGCalVFEProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
