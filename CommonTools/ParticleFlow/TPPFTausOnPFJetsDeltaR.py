import FWCore.ParameterSet.Config as cms

def TPPFTausOnPFJetsDeltaR(**kwargs):
  mod = cms.EDProducer('TPPFTausOnPFJetsDeltaR',
    enable = cms.required.bool,
    deltaR = cms.required.double,
    name = cms.untracked.string('No Name'),
    topCollection = cms.required.InputTag,
    bottomCollection = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
