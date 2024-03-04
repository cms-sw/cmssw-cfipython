import FWCore.ParameterSet.Config as cms

def CorrectedGenJetProducer(**kwargs):
  mod = cms.EDProducer('CorrectedGenJetProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
