import FWCore.ParameterSet.Config as cms

def GenMETProducer(**kwargs):
  mod = cms.EDProducer('GenMETProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
