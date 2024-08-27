import FWCore.ParameterSet.Config as cms

def HLTPFJetCollForElePlusJets(**kwargs):
  mod = cms.EDProducer('HLTPFJetCollForElePlusJets',
    HltElectronTag = cms.InputTag('triggerFilterObjectWithRefs'),
    SourceJetTag = cms.InputTag('jetCollection'),
    MinJetPt = cms.double(30),
    MaxAbsJetEta = cms.double(2.6),
    MinNJets = cms.uint32(1),
    minDeltaR = cms.double(0.5),
    MinSoftJetPt = cms.double(25),
    MinDeltaEta = cms.double(-1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
