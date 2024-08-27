import FWCore.ParameterSet.Config as cms

def GenJetConstituentSelector(**kwargs):
  mod = cms.EDProducer('GenJetConstituentSelector',
    src = cms.InputTag(''),
    cut = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
