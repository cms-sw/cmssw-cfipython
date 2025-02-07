import FWCore.ParameterSet.Config as cms

def HLTSumCaloJetTag(*args, **kwargs):
  mod = cms.EDFilter('HLTSumCaloJetTag',
    saveTags = cms.bool(True),
    Jets = cms.InputTag('hltJetCollection'),
    JetTags = cms.InputTag('hltJetTagCollection'),
    MinTag = cms.double(0),
    MaxTag = cms.double(999999),
    MinJetToSum = cms.int32(1),
    MaxJetToSum = cms.int32(-1),
    UseMeanValue = cms.bool(True),
    MatchByDeltaR = cms.bool(False),
    MaxDeltaR = cms.double(0.4),
    TriggerType = cms.int32(86),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
