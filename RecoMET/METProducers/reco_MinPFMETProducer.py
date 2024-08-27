import FWCore.ParameterSet.Config as cms

def reco_MinPFMETProducer(**kwargs):
  mod = cms.EDProducer('reco::MinPFMETProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
