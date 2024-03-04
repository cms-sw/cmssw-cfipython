import FWCore.ParameterSet.Config as cms

def LaserAlignmentProducer(**kwargs):
  mod = cms.EDProducer('LaserAlignmentProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
