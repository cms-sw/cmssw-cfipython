import FWCore.ParameterSet.Config as cms

def CorrectedPatMETProducer(**kwargs):
  mod = cms.EDProducer('CorrectedPatMETProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
