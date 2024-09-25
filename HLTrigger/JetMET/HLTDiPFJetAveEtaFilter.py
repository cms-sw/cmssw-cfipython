import FWCore.ParameterSet.Config as cms

def HLTDiPFJetAveEtaFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTDiPFJetAveEtaFilter',
    saveTags = cms.bool(True),
    inputJetTag = cms.InputTag('hltIterativeCone5CaloJets'),
    minPtAve = cms.double(100),
    minPtJet = cms.double(50),
    minDphi = cms.double(-1),
    minTagEta = cms.double(-1),
    maxTagEta = cms.double(1.4),
    minProbeEta = cms.double(2.7),
    maxProbeEta = cms.double(5.5),
    triggerType = cms.int32(85),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
