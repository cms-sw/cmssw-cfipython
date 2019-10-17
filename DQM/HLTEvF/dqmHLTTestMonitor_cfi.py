import FWCore.ParameterSet.Config as cms

dqmHLTTestMonitor = cms.EDAnalyzer('DaqTestHistograms',
  dqmPath = cms.untracked.string('DAQTEST/Test'),
  lumisectionRange = cms.untracked.uint32(25),
  numberOfHistograms = cms.untracked.uint32(10),
  mightGet = cms.optional.untracked.vstring
)
