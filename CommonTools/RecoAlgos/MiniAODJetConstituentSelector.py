import FWCore.ParameterSet.Config as cms

def MiniAODJetConstituentSelector(**kwargs):
  mod = cms.EDProducer('MiniAODJetConstituentSelector',
    src = cms.InputTag(''),
    cut = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
