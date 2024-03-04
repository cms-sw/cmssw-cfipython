import FWCore.ParameterSet.Config as cms

def CaloJetMETcorrInputProducer(**kwargs):
  mod = cms.EDProducer('CaloJetMETcorrInputProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
