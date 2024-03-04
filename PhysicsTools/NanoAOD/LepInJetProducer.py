import FWCore.ParameterSet.Config as cms

def LepInJetProducer(**kwargs):
  mod = cms.EDProducer('LepInJetProducer',
    src = cms.required.InputTag,
    srcEle = cms.required.InputTag,
    srcMu = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
