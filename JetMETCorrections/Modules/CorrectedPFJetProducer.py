import FWCore.ParameterSet.Config as cms

def CorrectedPFJetProducer(**kwargs):
  mod = cms.EDProducer('CorrectedPFJetProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
