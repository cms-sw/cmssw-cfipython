import FWCore.ParameterSet.Config as cms

def GenJetTauTaggerProducer(**kwargs):
  mod = cms.EDProducer('GenJetTauTaggerProducer',
    src = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
