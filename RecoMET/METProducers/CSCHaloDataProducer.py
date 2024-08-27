import FWCore.ParameterSet.Config as cms

def CSCHaloDataProducer(**kwargs):
  mod = cms.EDProducer('CSCHaloDataProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
