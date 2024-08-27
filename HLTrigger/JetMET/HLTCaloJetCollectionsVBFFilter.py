import FWCore.ParameterSet.Config as cms

def HLTCaloJetCollectionsVBFFilter(**kwargs):
  mod = cms.EDFilter('HLTCaloJetCollectionsVBFFilter',
    saveTags = cms.bool(True),
    inputTag = cms.InputTag('hltIterativeCone5CaloJets'),
    originalTag = cms.InputTag('hltIterativeCone5CaloJets'),
    SoftJetPt = cms.double(25),
    HardJetPt = cms.double(35),
    MinDeltaEta = cms.double(3),
    ThirdJetPt = cms.double(20),
    MaxAbsJetEta = cms.double(9999),
    MaxAbsThirdJetEta = cms.double(2.6),
    MinNJets = cms.uint32(2),
    TriggerType = cms.int32(85),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
