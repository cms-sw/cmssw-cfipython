import FWCore.ParameterSet.Config as cms

def CorrectedGenJetProducer(*args, **kwargs):
  mod = cms.EDProducer('CorrectedGenJetProducer',
    src = cms.InputTag(''),
    correctors = cms.VInputTag(),
    verbose = cms.untracked.bool(False),
    alias = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
