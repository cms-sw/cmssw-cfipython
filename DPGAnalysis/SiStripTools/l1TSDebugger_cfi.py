import FWCore.ParameterSet.Config as cms

l1TSDebugger = cms.EDAnalyzer('APVCyclePhaseDebuggerFromL1TS',
  l1TSCollection = cms.InputTag('scalersRawToDigi')
)
