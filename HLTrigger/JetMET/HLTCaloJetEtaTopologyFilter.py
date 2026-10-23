import FWCore.ParameterSet.Config as cms

def HLTCaloJetEtaTopologyFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTCaloJetEtaTopologyFilter',
    saveTags = cms.bool(True),
    inputJetTag = cms.InputTag('hltIterativeCone5CaloJets'),
    minPtJet = cms.double(50),
    minJetEta = cms.double(-1),
    maxJetEta = cms.double(1.4),
    applyAbsToJet = cms.bool(False),
    triggerType = cms.int32(85),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
