import FWCore.ParameterSet.Config as cms

def CorrectedCaloJetProducer(*args, **kwargs):
  mod = cms.EDProducer('CorrectedCaloJetProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
