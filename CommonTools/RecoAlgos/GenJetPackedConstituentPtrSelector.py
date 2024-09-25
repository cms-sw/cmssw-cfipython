import FWCore.ParameterSet.Config as cms

def GenJetPackedConstituentPtrSelector(*args, **kwargs):
  mod = cms.EDProducer('GenJetPackedConstituentPtrSelector',
    src = cms.InputTag(''),
    cut = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
