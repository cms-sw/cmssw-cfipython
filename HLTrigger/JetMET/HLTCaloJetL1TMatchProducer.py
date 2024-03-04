import FWCore.ParameterSet.Config as cms

def HLTCaloJetL1TMatchProducer(**kwargs):
  mod = cms.EDProducer('HLTCaloJetL1TMatchProducer',
    jetsInput = cms.InputTag('hltAntiKT5PFJets'),
    L1Jets = cms.InputTag('hltCaloStage2Digis'),
    DeltaR = cms.double(0.5),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
