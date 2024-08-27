import FWCore.ParameterSet.Config as cms

def AddAllIntsProducer(**kwargs):
  mod = cms.EDProducer('AddAllIntsProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
