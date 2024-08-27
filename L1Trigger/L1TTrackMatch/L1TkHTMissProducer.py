import FWCore.ParameterSet.Config as cms

def L1TkHTMissProducer(**kwargs):
  mod = cms.EDProducer('L1TkHTMissProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
