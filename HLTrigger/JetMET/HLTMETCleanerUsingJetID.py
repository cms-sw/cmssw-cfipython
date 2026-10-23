import FWCore.ParameterSet.Config as cms

def HLTMETCleanerUsingJetID(*args, **kwargs):
  mod = cms.EDProducer('HLTMETCleanerUsingJetID',
    minPt = cms.double(20),
    maxEta = cms.double(5),
    metLabel = cms.InputTag('hltMet'),
    jetsLabel = cms.InputTag('hltAntiKT4CaloJets'),
    goodJetsLabel = cms.InputTag('hltCaloJetIDPassed'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
