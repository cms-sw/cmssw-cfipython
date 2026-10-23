import FWCore.ParameterSet.Config as cms

def PFJetConstituentSelector(*args, **kwargs):
  mod = cms.EDProducer('PFJetConstituentSelector',
    src = cms.InputTag(''),
    cut = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
