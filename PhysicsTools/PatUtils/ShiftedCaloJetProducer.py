import FWCore.ParameterSet.Config as cms

def ShiftedCaloJetProducer(**kwargs):
  mod = cms.EDProducer('ShiftedCaloJetProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
