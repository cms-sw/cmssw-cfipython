import FWCore.ParameterSet.Config as cms

def FixedGridRhoProducer(**kwargs):
  mod = cms.EDProducer('FixedGridRhoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
