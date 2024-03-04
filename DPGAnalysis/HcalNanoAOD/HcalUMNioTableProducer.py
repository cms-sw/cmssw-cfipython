import FWCore.ParameterSet.Config as cms

def HcalUMNioTableProducer(**kwargs):
  mod = cms.EDProducer('HcalUMNioTableProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
