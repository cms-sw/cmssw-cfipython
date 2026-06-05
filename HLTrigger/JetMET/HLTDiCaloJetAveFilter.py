import FWCore.ParameterSet.Config as cms

def HLTDiCaloJetAveFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTDiCaloJetAveFilter',
    saveTags = cms.bool(True),
    inputJetTag = cms.InputTag('hltIterativeCone5CaloJets'),
    minPtAve = cms.double(100),
    minPtJet3 = cms.double(99999),
    minDphi = cms.double(-1),
    triggerType = cms.int32(85),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
