import FWCore.ParameterSet.Config as cms

def PileupJPTJetIdProducer(**kwargs):
  mod = cms.EDProducer('PileupJPTJetIdProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
