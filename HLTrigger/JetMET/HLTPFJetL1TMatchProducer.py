import FWCore.ParameterSet.Config as cms

def HLTPFJetL1TMatchProducer(**kwargs):
  mod = cms.EDProducer('HLTPFJetL1TMatchProducer',
    jetsInput = cms.InputTag('hltAntiKT5PFJets'),
    L1Jets = cms.InputTag('hltCaloStage2Digis'),
    DeltaR = cms.double(0.5),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
