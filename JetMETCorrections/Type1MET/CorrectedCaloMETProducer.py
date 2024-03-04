import FWCore.ParameterSet.Config as cms

def CorrectedCaloMETProducer(**kwargs):
  mod = cms.EDProducer('CorrectedCaloMETProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
