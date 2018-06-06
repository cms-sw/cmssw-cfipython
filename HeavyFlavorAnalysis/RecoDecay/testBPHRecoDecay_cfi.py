import FWCore.ParameterSet.Config as cms

testBPHRecoDecay = cms.EDAnalyzer('TestBPHRecoDecay',
  patMuonLabel = cms.string(''),
  ccCandsLabel = cms.string(''),
  pfCandsLabel = cms.string(''),
  pcCandsLabel = cms.string(''),
  gpCandsLabel = cms.string(''),
  outDump = cms.string('dump.txt'),
  outHist = cms.string('hist.root')
)
