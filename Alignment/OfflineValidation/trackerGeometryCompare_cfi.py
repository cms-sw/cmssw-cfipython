import FWCore.ParameterSet.Config as cms

trackerGeometryCompare = cms.EDAnalyzer('TrackerGeometryCompare',
  levels = cms.untracked.vstring(),
  fromDD4hep = cms.untracked.bool(False),
  writeToDB = cms.untracked.bool(False),
  moduleList = cms.untracked.string('moduleList.txt'),
  inputROOTFile1 = cms.untracked.string('IDEAL'),
  inputROOTFile2 = cms.untracked.string('idealtracker2.root'),
  treeNameAlign = cms.untracked.string('alignTree'),
  treeNameDeform = cms.untracked.string('alignTreeDeformations'),
  outputFile = cms.untracked.string('output.root'),
  surfDir = cms.untracked.string('.'),
  weightBy = cms.untracked.string('DetUnit'),
  setCommonTrackerSystem = cms.untracked.string('NONE'),
  detIdFlag = cms.untracked.bool(False),
  detIdFlagFile = cms.untracked.string('blah.txt'),
  weightById = cms.untracked.bool(False),
  weightByIdFile = cms.untracked.string('blah2.txt'),
  mightGet = cms.optional.untracked.vstring
)
