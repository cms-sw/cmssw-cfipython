import FWCore.ParameterSet.Config as cms

hcalRaddamMuon = cms.EDAnalyzer('HcalRaddamMuon',
  hlTriggerResults = cms.untracked.InputTag('TriggerResults', '', 'HLT'),
  muonSource = cms.untracked.InputTag('muons'),
  verbosity = cms.untracked.int32(0),
  useRaw = cms.untracked.int32(0),
  isAOD = cms.bool(False),
  maxDepth = cms.untracked.int32(4)
)
