import FWCore.ParameterSet.Config as cms

def GenJetFlavourTableProducer(*args, **kwargs):
  mod = cms.EDProducer('GenJetFlavourTableProducer',
    src = cms.required.InputTag,
    jetFlavourInfos = cms.required.InputTag,
    name = cms.required.string,
    cut = cms.required.string,
    deltaR = cms.required.double,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
