import FWCore.ParameterSet.Config as cms

def HLTPFJetEtaTopologyFilter(**kwargs):
  mod = cms.EDFilter('HLTPFJetEtaTopologyFilter',
    saveTags = cms.bool(True),
    inputJetTag = cms.InputTag('hltIterativeCone5CaloJets'),
    minPtJet = cms.double(50),
    minJetEta = cms.double(-1),
    maxJetEta = cms.double(1.4),
    applyAbsToJet = cms.bool(False),
    triggerType = cms.int32(85),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
