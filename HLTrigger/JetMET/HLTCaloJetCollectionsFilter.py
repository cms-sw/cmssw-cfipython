import FWCore.ParameterSet.Config as cms

def HLTCaloJetCollectionsFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTCaloJetCollectionsFilter',
    saveTags = cms.bool(True),
    inputTag = cms.InputTag('hltIterativeCone5CaloJets'),
    originalTag = cms.InputTag('hltIterativeCone5CaloJets'),
    MinJetPt = cms.double(30),
    MaxAbsJetEta = cms.double(2.6),
    MinNJets = cms.uint32(1),
    triggerType = cms.int32(85),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
