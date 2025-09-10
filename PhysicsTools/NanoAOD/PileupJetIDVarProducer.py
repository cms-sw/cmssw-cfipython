import FWCore.ParameterSet.Config as cms

def PileupJetIDVarProducer(*args, **kwargs):
  mod = cms.EDProducer('PileupJetIDVarProducer',
    srcJet = cms.required.InputTag,
    srcPileupJetId = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
