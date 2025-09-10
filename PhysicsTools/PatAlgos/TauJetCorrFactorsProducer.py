import FWCore.ParameterSet.Config as cms

def TauJetCorrFactorsProducer(*args, **kwargs):
  mod = cms.EDProducer('TauJetCorrFactorsProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
