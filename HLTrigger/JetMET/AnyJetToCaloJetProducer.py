import FWCore.ParameterSet.Config as cms

def AnyJetToCaloJetProducer(*args, **kwargs):
  mod = cms.EDProducer('AnyJetToCaloJetProducer',
    Source = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
