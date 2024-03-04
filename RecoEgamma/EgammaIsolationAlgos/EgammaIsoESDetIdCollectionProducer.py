import FWCore.ParameterSet.Config as cms

def EgammaIsoESDetIdCollectionProducer(**kwargs):
  mod = cms.EDProducer('EgammaIsoESDetIdCollectionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
