import FWCore.ParameterSet.Config as cms

def HLTCaloJetCollectionsFilter(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
