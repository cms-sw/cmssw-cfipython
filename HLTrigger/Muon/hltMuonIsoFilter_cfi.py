import FWCore.ParameterSet.Config as cms

hltMuonIsoFilter = cms.EDFilter('HLTMuonIsoFilter',
  saveTags = cms.bool(True),
  CandTag = cms.InputTag('hltL3MuonCandidates'),
  PreviousCandTag = cms.InputTag(''),
  MinN = cms.int32(1),
  DepTag = cms.VInputTag('hltL3MuonIsolations'),
  IsolatorPSet = cms.PSet()
)
