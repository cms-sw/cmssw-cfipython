import FWCore.ParameterSet.Config as cms

siPhase2BadStripChannelBuilder = cms.EDAnalyzer('SiPhase2BadStripChannelBuilder',
  SinceAppendMode = cms.required.bool,
  IOVMode = cms.required.string,
  Record = cms.required.string,
  doStoreOnDB = cms.required.bool,
  TimeFromEndRun = cms.untracked.bool(False),
  TimeFromStartOfRunRange = cms.untracked.bool(False),
  printDebug = cms.untracked.bool(False),
  popConAlgo = cms.uint32(1),
  badComponentsFraction = cms.double(0.01),
  mightGet = cms.optional.untracked.vstring
)
