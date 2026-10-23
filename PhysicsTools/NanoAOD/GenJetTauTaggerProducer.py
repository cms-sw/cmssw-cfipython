import FWCore.ParameterSet.Config as cms

def GenJetTauTaggerProducer(*args, **kwargs):
  mod = cms.EDProducer('GenJetTauTaggerProducer',
    src = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
