import FWCore.ParameterSet.Config as cms

def GenVisTauProducer(**kwargs):
  mod = cms.EDProducer('GenVisTauProducer',
    src = cms.required.InputTag,
    srcGenParticles = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
