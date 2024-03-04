import FWCore.ParameterSet.Config as cms

def HcalUHTRTableProducer(**kwargs):
  mod = cms.EDProducer('HcalUHTRTableProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
