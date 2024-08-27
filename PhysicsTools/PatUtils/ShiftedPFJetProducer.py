import FWCore.ParameterSet.Config as cms

def ShiftedPFJetProducer(**kwargs):
  mod = cms.EDProducer('ShiftedPFJetProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
