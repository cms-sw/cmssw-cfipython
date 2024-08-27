import FWCore.ParameterSet.Config as cms

def TauJetCorrFactorsProducer(**kwargs):
  mod = cms.EDProducer('TauJetCorrFactorsProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
