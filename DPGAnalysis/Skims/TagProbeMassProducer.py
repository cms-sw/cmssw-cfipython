import FWCore.ParameterSet.Config as cms

def TagProbeMassProducer(**kwargs):
  mod = cms.EDProducer('TagProbeMassProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
