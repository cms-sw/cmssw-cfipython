import FWCore.ParameterSet.Config as cms

def trgMatchMETProducer(**kwargs):
  mod = cms.EDProducer('trgMatchMETProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
