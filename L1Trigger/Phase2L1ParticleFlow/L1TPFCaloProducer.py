import FWCore.ParameterSet.Config as cms

def L1TPFCaloProducer(**kwargs):
  mod = cms.EDProducer('L1TPFCaloProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
