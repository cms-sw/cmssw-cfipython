import FWCore.ParameterSet.Config as cms

def JVFJetIdProducer(**kwargs):
  mod = cms.EDProducer('JVFJetIdProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
