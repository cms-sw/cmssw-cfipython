import FWCore.ParameterSet.Config as cms

def AnyJetToCaloJetProducer(**kwargs):
  mod = cms.EDProducer('AnyJetToCaloJetProducer',
    Source = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
