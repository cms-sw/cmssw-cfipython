import FWCore.ParameterSet.Config as cms

HGCalEEParametersWriter = cms.EDAnalyzer('PHGCalParametersDBBuilder',
  name = cms.string('HGCalEESensitive'),
  name2 = cms.string('HGCalEE'),
  nameW = cms.string('HGCalEEWafer'),
  nameC = cms.string('HGCalEECell'),
  nameT = cms.string('HGCal'),
  fromDD4hep = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
