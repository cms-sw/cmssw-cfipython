import FWCore.ParameterSet.Config as cms

def Phase2L1TGMTProducer(**kwargs):
  mod = cms.EDProducer('Phase2L1TGMTProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
