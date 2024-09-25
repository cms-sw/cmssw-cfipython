import FWCore.ParameterSet.Config as cms

def CorrectedGenJetProducer(*args, **kwargs):
  mod = cms.EDProducer('CorrectedGenJetProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
