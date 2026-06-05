import FWCore.ParameterSet.Config as cms

def TPPFTausOnPFJetsDeltaR(*args, **kwargs):
  mod = cms.EDProducer('TPPFTausOnPFJetsDeltaR',
    enable = cms.required.bool,
    deltaR = cms.required.double,
    name = cms.untracked.string('No Name'),
    topCollection = cms.required.InputTag,
    bottomCollection = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
