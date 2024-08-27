import FWCore.ParameterSet.Config as cms

def HcalDigiSortedTableProducer(**kwargs):
  mod = cms.EDProducer('HcalDigiSortedTableProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
