import FWCore.ParameterSet.Config as cms

def PileupJetIDVarProducer(**kwargs):
  mod = cms.EDProducer('PileupJetIDVarProducer',
    srcJet = cms.required.InputTag,
    srcPileupJetId = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
