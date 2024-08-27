import FWCore.ParameterSet.Config as cms

def FFTJetProducer(**kwargs):
  mod = cms.EDProducer('FFTJetProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
