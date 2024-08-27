import FWCore.ParameterSet.Config as cms

def PATCompositeCandidateProducer(**kwargs):
  mod = cms.EDProducer('PATCompositeCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
