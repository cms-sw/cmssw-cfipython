import FWCore.ParameterSet.Config as cms

def EmptyHepMCProducer(**kwargs):
  mod = cms.EDProducer('EmptyHepMCProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
