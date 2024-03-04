import FWCore.ParameterSet.Config as cms

def PileupJetIdProducer(**kwargs):
  mod = cms.EDProducer('PileupJetIdProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
