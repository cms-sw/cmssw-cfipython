import FWCore.ParameterSet.Config as cms

def LepInJetProducer(*args, **kwargs):
  mod = cms.EDProducer('LepInJetProducer',
    src = cms.required.InputTag,
    srcEle = cms.required.InputTag,
    srcMu = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
