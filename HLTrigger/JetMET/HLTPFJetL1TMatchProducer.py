import FWCore.ParameterSet.Config as cms

def HLTPFJetL1TMatchProducer(*args, **kwargs):
  mod = cms.EDProducer('HLTPFJetL1TMatchProducer',
    jetsInput = cms.InputTag('hltAntiKT5PFJets'),
    L1Jets = cms.InputTag('hltCaloStage2Digis'),
    DeltaR = cms.double(0.5),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
