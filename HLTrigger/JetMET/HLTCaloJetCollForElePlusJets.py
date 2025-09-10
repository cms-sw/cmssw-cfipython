import FWCore.ParameterSet.Config as cms

def HLTCaloJetCollForElePlusJets(*args, **kwargs):
  mod = cms.EDProducer('HLTCaloJetCollForElePlusJets',
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
