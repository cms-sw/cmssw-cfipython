import FWCore.ParameterSet.Config as cms

def L1TPFMetNoMuProducer(**kwargs):
  mod = cms.EDProducer('L1TPFMetNoMuProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
