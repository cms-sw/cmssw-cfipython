import FWCore.ParameterSet.Config as cms

hcalHBHEMuonAnalysis = cms.EDAnalyzer('HcalHBHENewMuonAnalyzer',
  hbheMuonLabel = cms.InputTag('alcaHcalHBHEMuonProducer', 'hbheMuon'),
  useRaw = cms.int32(0),
  maxDepth = cms.untracked.int32(4),
  mightGet = cms.optional.untracked.vstring
)
