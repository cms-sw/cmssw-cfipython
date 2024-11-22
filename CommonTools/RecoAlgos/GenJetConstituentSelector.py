import FWCore.ParameterSet.Config as cms

def GenJetConstituentSelector(*args, **kwargs):
  mod = cms.EDProducer('GenJetConstituentSelector',
    src = cms.InputTag(''),
    cut = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
