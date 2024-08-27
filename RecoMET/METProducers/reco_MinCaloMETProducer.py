import FWCore.ParameterSet.Config as cms

def reco_MinCaloMETProducer(**kwargs):
  mod = cms.EDProducer('reco::MinCaloMETProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
