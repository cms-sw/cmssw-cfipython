import FWCore.ParameterSet.Config as cms

def trgMatchedMETProducer(**kwargs):
  mod = cms.EDProducer('trgMatchedMETProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
