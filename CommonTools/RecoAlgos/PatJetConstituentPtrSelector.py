import FWCore.ParameterSet.Config as cms

def PatJetConstituentPtrSelector(*args, **kwargs):
  mod = cms.EDProducer('PatJetConstituentPtrSelector',
    src = cms.InputTag(''),
    cut = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
