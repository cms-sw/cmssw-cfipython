import FWCore.ParameterSet.Config as cms

def TCMETProducer(**kwargs):
  mod = cms.EDProducer('TCMETProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
