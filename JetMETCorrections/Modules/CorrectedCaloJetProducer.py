import FWCore.ParameterSet.Config as cms

def CorrectedCaloJetProducer(**kwargs):
  mod = cms.EDProducer('CorrectedCaloJetProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
